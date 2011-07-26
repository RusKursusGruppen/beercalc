# -*- coding: utf-8 -*-
u""
import json
import shutil
import os.path as path

import app.utils.date as dateutils
from app.model.usage import Usage
from app.model.account import Accounts
from app.model.inventory import Inventory

class Document(object):
    def __init__(self, usage=None, accounts=None, inventory=None, date=None, comment=None, filepath=None, version=1):
        self.date = date
        self.comment = comment

        self.inventory = inventory or Inventory()
        self.accounts = accounts or Accounts()
        self.usage = usage or Usage(self.inventory, self.accounts)
        self.version = version
        self.filepath = filepath

    def save(self, comment = u"", filepath=None):
        self.date = dateutils.now()
        self.comment = comment
        
        filepath = filepath or self.filepath

        if filepath is None:
            raise Exception("No path specified")

        try:
            current = Document.load(filepath)
        except IOError:
            pass
        else:
            dateformatted = current.date.astimezone(dateutils.utc).strftime("%Y.%m.%d.%H.%M.%S")
            shutil.move(filepath, filepath + "." + dateformatted)
        
        with open(filepath, "w") as f:
            json.dump(self.export(), f)
        
    def export(self):
        date = None
        if self.date is not None:
            date = dateutils.totuple(self.date)
        
        return {
            "version": self.version,
            "comment": self.comment,
            "date": date,
            "usage": self.usage.export(),
            "accounts": self.accounts.export(),
            "inventory": self.inventory.export()
        }

    @staticmethod
    def load(filepath):
        with open(filepath, "r") as f:
            return Document.create(json.load(f), filepath)

    @staticmethod
    def create(data, filepath = None):
        version = data["version"]
        
        if version == 1:
            inventory = Inventory.create(data["inventory"])
            accounts = Accounts.create(data["accounts"])
            usage = Usage.create(data["usage"], inventory, accounts)
            comment = data["comment"]
            
            date = data["date"]
            if date is not None:
                date = dateutils.fromtuple(date)

        else:
            raise VersionError("Unknown document version: " %(repr(version),))

        return Document(
            usage = usage,
            accounts = accounts,
            inventory = inventory,
            date = date,
            comment = comment,
            filepath = filepath,
            version = version
        )

        

