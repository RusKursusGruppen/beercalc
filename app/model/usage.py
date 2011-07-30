# -*- coding: utf-8 -*-
u""
from account import Accounts, Account
from inventory import Inventory, Product, Purchase
from collections import defaultdict

from copy import deepcopy, copy

class Usage(object):
    def __init__(self, inventory, accounts):
        self.inventory = inventory
        self.accounts = accounts
        self.counter = defaultdict(int)
        self.total_counts = defaultdict(int)
        self.old_total_counts = defaultdict(int)
        self.profits = defaultdict(int)

    def set_profit(self, product_id, amount):
        try:
            product = self.inventory.get_product(product_id)
        except KeyError:
            return
        self.profits[product] = amount

    def update(self, account_id, product_id, amount):
        try:
            account = self.accounts.get_account(account_id)
            product = self.inventory.get_product(product_id)
        except KeyError:
            return

        self.counter[account, product] += amount
        self.total_counts[product] += amount
        self.old_total_counts[product] += amount
    
    def reset(self):
        self.counter.clear()
        self.total_counts.clear()
        self.profits.clear()
        

    def preview(self):
        usage = deepcopy(self)
        
        usage.commit(log_transaction=False)

        data = {
            "accounts": [],
            "prices": [],
        }

        for id, account_after in usage.accounts.accounts.items():
            data["accounts"].append((id, account_after.get_balance() - self.accounts.get_account(id).get_balance()))

        for id, product in usage.inventory.products.items():
            try:
                price = product.get_price(1, usage.old_total_counts[product])
            except ZeroDivisionError:
                price = 0
            print "Price:", price
            data["prices"].append((id, -price))

        return data

    def commit(self, log_transaction=True):
        self.old_total_counts = copy(self.total_counts)
        for product, amount in self.profits.items():
            product.add_profit(amount)

        for (account, product), count in sorted(self.counter.items(), key=lambda x: x[0][0].name):
            if count == 0:
                continue
        
            if account.istutor:
                price = product.get_fixedprice(count)
            else:
                price = product.get_price(count, self.total_counts[product])

            account.add_transaction(u"Køb af %d %s" % (count, product.name,), -price)
            if log_transaction:
                product.income.add_transaction(u"Køb fra %s af %d stk." % (account.id, count), price)
            self.total_counts[product] -= count
        
        self.reset()

    def export(self):
        return {
            "counter": [
                {
                    "account_id": account.id,
                    "product_id": product.id,
                    "count": count
                }
                for (account, product), count in self.counter.items()
            ],
            "profits": [ 
                {
                    "product_id": product.id,
                    "amount": amount
                }
                for product, amount in self.profits.items()
            ]
        }

    @staticmethod
    def create(data, inventory, accounts):
        usage = Usage(inventory, accounts)
        for c in data["counter"]:
            usage.update(c["account_id"], c["product_id"], c["count"])
        for p in data["profits"]:
            usage.set_profit(p["product_id"], p["amount"])
        return usage
