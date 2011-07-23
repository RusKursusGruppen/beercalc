# -*- coding: utf-8 -*-

from app.model.document import Document

try:
    document = Document.load("savedir/save.beer")
except IOError:
    document = Document()

accounts = document.accounts
inventory = document.inventory
usage = document.usage
