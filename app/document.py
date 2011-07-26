# -*- coding: utf-8 -*-

from app.model.document import Document

try:
    document = Document.load("savedir/save.beer")
except IOError:
    document = Document()
    document.save(filepath="savedir/save.beer", comment=u"New file")

accounts = document.accounts
inventory = document.inventory
usage = document.usage
