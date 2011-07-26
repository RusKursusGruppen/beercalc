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
            if count == 0:
                continue
            price = product.get_price(count, self.total_counts[product])
            account.add_transaction(u"Køb af %d %s" % (count, product.name,), -price)
            product.income.add_transaction(u"Køb fra %s af %d stk." % (account.id, count), price)
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
