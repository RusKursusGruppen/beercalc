#!/usr/bin/python2 -B
# -*- coding: utf-8 -*-
import sys
from os.path import dirname, join

# Prepend 3rd-party to path
sys.path[0] = join(dirname(__file__))
sys.path.insert(0, join(sys.path[0], "3rd-party"))


from random import randint
from pprint import pprint
from app.model.inventory import Purchase, Product
from app.model.account import Account
from app.model.document import Document
import app.utils.date as dateutils

document = Document(date=dateutils.now())
accounts = document.accounts
inventory = document.inventory
usage = document.usage

for i in range(1,50):
    account = Account(name=u"Account %d" % (i,))
    accounts.add_account(account)

product1 = Product(u"Guld øl")
product1.add_purchase(Purchase(u"Guld Tuborg", 270000, 300))
product1.add_purchase(Purchase(u"Harboe Guld", 7000, 35))
inventory.add_product(product1)
product2 = Product(u"Sodavand")
product2.add_purchase(Purchase(u"Hindbærbrus", 27000, 60))
product2.add_purchase(Purchase(u"Cola", 27000, 60))
inventory.add_product(product2)

product1.stock = 0
product2.stock = 0

for account in accounts.list_by_name():
    usage.update(account.id, product1.id, randint(4,12))
    usage.update(account.id, product2.id, randint(1,2))

usage.commit()

export1 = document.export()
export2 = Document.create(export1).export()

document.save("savedir/save.beer")
