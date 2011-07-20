# -*- coding: utf-8 -*-
u""
import app.model.usage 
import app.model.inventory
import app.model.account
import app.model.database
def run():
    inventory = app.model.inventory.Inventory()
    accounts = app.model.account.Accounts()
    usage = app.model.usage.Usage(inventory, accounts)
    
    from random import randint
    from pprint import pprint

    for i in range(1,4):
        account = app.model.account.Account(name=u"Account %d" % (i,))
        accounts.add_account(account)

    product1 = app.model.inventory.Product(u"Guld øl")
    product1.add_purchase(app.model.inventory.Purchase(u"Guld Tuborg", 200.00, 45))
    product1.add_purchase(app.model.inventory.Purchase(u"Harboe Guld", 70.00, 35))
    inventory.add_product(product1)
    product2 = app.model.inventory.Product(u"Sodavand")
    product2.add_purchase(app.model.inventory.Purchase(u"Hindbærbrus", 70.00, 45))
    product2.add_purchase(app.model.inventory.Purchase(u"Cola", 70.00, 35))
    inventory.add_product(product2)

    product1.update_stock(80)

    for account in accounts.list_by_name():
        usage.update(account.id, product1.id, randint(4,12))
        usage.update(account.id, product2.id, randint(4,12))
    
    app.model.database.save(usage, "/home/bjorn/projects/beercalc/savedir")
    


