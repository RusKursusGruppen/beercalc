# -*- coding: utf-8 -*-
u""
from account import Accounts, Account
from inventory import Inventory, Product, Purchase
from collections import defaultdict


class Usage(object):
    def __init__(self, inventory, accounts):
        self.inventory = inventory
        self.accounts = accounts
        self.counter = defaultdict(int)
        self.total_counts = defaultdict(int)

    def update(self, account_id, product_id, amount):
        account = self.accounts.get_account(account_id)
        product = self.inventory.get_product(product_id)
        self.counter[account, product] += amount
        self.total_counts[product] += amount
    
    def commit(self):
        for (account, product), count in self.counter.items():
            price = product.sell(count, self.total_counts[product])
            account.add_transaction(u"Køb af %d %s" % (count, product.name,), price)
            self.total_counts[product] -= count

        self.counter.clear()
        self.total_counts.clear()
    
    def export(self):
        return {
            "counter": [
                {
                    "account_id": account.id,
                    "product_id": product.id,
                    "count": count
                }
                for (account, product), count in self.counter.items()
            ]
        }


    @staticmethod
    def create(data, inventory, accounts):
        usage = Usage(inventory, accounts)
        for c in data["counter"]:
            usage.update(c["account_id"], c["product_id"], c["count"])
        return usage

if __name__ == "__main__":
    from random import randint
    from pprint import pprint
    accounts = Accounts()

    for i in range(1,4):
        account = Account(name=u"Account %d" % (i,))
        accounts.add_account(account)

    inventory = Inventory()
    product1 = Product(u"Guld øl")
    product1.add_purchase(Purchase(u"Guld Tuborg", 200.00, 45))
    product1.add_purchase(Purchase(u"Harboe Guld", 70.00, 35))
    inventory.add_product(product1)
    product2 = Product(u"Sodavand")
    product2.add_purchase(Purchase(u"Hindbærbrus", 70.00, 45))
    product2.add_purchase(Purchase(u"Cola", 70.00, 35))
    inventory.add_product(product2)

    usage = Usage(inventory, accounts)

    product1.update_stock(80)

    for account in accounts.list_by_name():
        usage.update(account.id, product1.id, randint(4,12))
        usage.update(account.id, product2.id, randint(4,12))

    pprint(Usage.create(usage.export(), inventory, accounts).export())
    usage.commit()
    pprint(usage.export())
