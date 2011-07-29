# -*- coding: utf-8 -*-
u""
import json
import shutil
import os.path as path

from uuid import uuid4
import app.utils.date as dateutils
from app.model.usage import Usage
from app.model.account import Accounts, Account
from app.model.inventory import Inventory

class Document(object):
    def __init__(self, usage=None, accounts=None, inventory=None, date=None, comment=None, filepath=None, version=1, cash_in_hand=None, id_=None, title=None):
        self.date = date
        self.comment = comment
        self.title = title
        
        self.id = id_ or uuid4().hex

        self.inventory = inventory or Inventory()
        self.accounts = accounts or Accounts()
        self.usage = usage or Usage(self.inventory, self.accounts)
        self.version = version
        self.cash_in_hand = cash_in_hand or Account()
        self.filepath = filepath

    def save(self, comment = u"", filepath=None):
        self.date = dateutils.now()
        self.comment = comment
        self.version = 2
        
        filepath = filepath or self.filepath
        
        self.filepath = filepath

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
            "inventory": self.inventory.export(),
            "cash_in_hand": self.cash_in_hand.export(),
            "title": self.title,
            "id": self.id,
        }

    @staticmethod
    def load(filepath):
        with open(filepath, "r") as f:
            return Document.create(json.load(f), filepath)

    @staticmethod
    def create(data, filepath = None):
        version = data["version"]
        
        if version >= 1 and version <= 2:
            inventory = Inventory.create(data["inventory"])
            accounts = Accounts.create(data["accounts"])
            usage = Usage.create(data["usage"], inventory, accounts)
            comment = data["comment"]
            cash_in_hand = Account.create(data["cash_in_hand"])
            date = data["date"]
            if date is not None:
                date = dateutils.fromtuple(date)
            
            if version >= 2:
                id_ = data["id"]
                title = data["title"]
            else:
                id_ = uuid4().hex
                title = None
        else:
            raise VersionError("Unknown document version: " %(repr(version),))

        return Document(
            usage = usage,
            accounts = accounts,
            inventory = inventory,
            date = date,
            comment = comment,
            filepath = filepath,
            version = version,
            cash_in_hand = cash_in_hand,
            title = title,
            id_ = id_
        )

        

