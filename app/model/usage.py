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

    def reset(self):
        self.counter.clear()
        self.total_counts.clear()
        self.profits.clear()

    def get_approx_pricelist(self):
        for id, product in self.inventory.products.items():
            try:
                yield id, -product.get_price(1, self.total_counts[product])
            except ZeroDivisionError:
                yield id, 0

    def preview(self):
        usage = deepcopy(self)
        usage.commit()

        for id, account_after in usage.accounts.accounts.items():
            yield id, account_after.get_balance() - self.accounts.get_account(id).get_balance()

    def commit(self):
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
