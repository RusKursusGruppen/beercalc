# -*- coding: utf-8 -*-
u""
import app.utils.date as dateutils
import app.model.usage
import json
import shutil
import os.path as path

def save(data, savedir, comment = u""):
    data = {
        "comment": comment,
        "date": dateutils.totuple(dateutils.now()),
        "data": data.export()
    }
    
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
