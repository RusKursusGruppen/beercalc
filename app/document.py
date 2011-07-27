# -*- coding: utf-8 -*-

from app.model.document import Document

try:
    doc = [Document.load("savedir/save.beer")]
except IOError:
    doc = [Document()]
    doc[0].save(filepath="savedir/save.beer", comment=u"New file")

def document():
    return doc[0]

def usage():
    return document().usage

def inventory():
    return document().inventory

def accounts():
    return document().accounts

def set_document(document):
    doc[0] = document
