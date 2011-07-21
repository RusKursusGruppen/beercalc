# -*- coding: utf-8 -*-
u""
import app.utils.date as dateutils
import app.model.usage
import json
import shutil
import os.path as path

class Document(object)
    def __init__(self, usage=None, datesaved=None, savecomment=None, filepath=None):
        self.date = datesaved
        self.comment = savecomment
        self.usage = usage or app.model.usage.Usage()
        self.formatversion = version

    def save(data, savedir, comment = u""):
        self.date = dateutils.totuple(dateutils.now())
        self.comment = comment
        self.formatversion = 1
        
        currentpath = path.join(savedir, "save.beer")
        
        try:
            current = load(savedir)
        except IOError:
            pass
        else:
            date = dateutils.fromtuple(current["date"])
            dateformatted = date.astimezone(dateutils.utc).strftime("%Y.%m.%d.%H.%M.%S")
            shutil.move(currentpath, currentpath + "." + dateformatted)
        
        with open(currentpath, "w") as f:
            json.dump(data, f)
        

    def load(savedir, filename="save.beer"):
        filepath = path.join(savedir, filename)
        
        with open(filepath, "r") as f:
            return json.load(f)
    
    def export(self):
        return {
            "formatversion": self.formatversion,
            "comment": self.comment,
            "date": self.date,
            "usage": self.data.export()
        }

    @staticmethod
    def create(data):
        version = data["formatversion"]
        
        if version == 1:
            return Document(
        else:
            raise VersionError("Unknown version: " %(repr(version),))

        
        

