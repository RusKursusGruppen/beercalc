# -*- coding: utf-8 -*-
u""

from uuid import uuid4
from datetime import datetime
from email.utils import parsedate, formatdate
import app.utils.date as dateutils

class Inventory(object):
    def __init__(self, products=None):
        self.products = products or dict()

    def get_product(self, id_):
        return self.products[id_]
    
    def add_product(self, product):
        self.products[product.id] = product
    
    def list_by_name(self):
        ret = self.products.values()
        ret.sort(key=lambda x: x.name)
        return ret

    def export(self):
        return [p.export() for p in self.products.values()]
    
    @staticmethod
    def create(data):
        ret = Inventory()
        for p in data:
            ret.add_product(Product.create(p))
        return ret


class Product(object):
    def __init__(self, name=u"", stock=0, income=0, id_=None, purchases=None):
        self.purchases = purchases or []
        self.name = name
        self.stock = stock
        self.income = income
        self.id = id_ or unicode(uuid4().hex)
    
    def add_purchase(self, purchase):
        self.purchases.append(purchase)
    
    def total_purchase(self):
        return sum(x.price for x in self.purchases)
    
    def update_stock(self, count):
        self.stock = count

    def get_base_unit_price(self):
        return self.total_purchase() / sum(x.quantity for x in self.purchases)
    
    def get_stock_diff(self, sold_total):
        return sum(x.quantity for x in self.purchases) - self.stock - sold_total
    
    def get_value_diff(self, sold_total):
        return self.get_base_unit_price() * self.get_stock_diff(sold_total)
    
    def add_income(self, amount):
        self.income += amount

    def sell(self, sold_individual, sold_total):
        sell_value = sold_individual * (self.total_purchase() - self.stock * self.get_base_unit_price() - self.income) / sold_total

        self.income += sell_value
        return sell_value
    
    def sell_fixed(self, count=0, price=None):
        if price is None:
            price = self.get_base_unit_price()

        self.add_income(price * count)
    
    def export(self):
        return {
            "id": self.id,
            "name": self.name,
            "stock": self.stock,
            "income": self.income,
            "purchases": [p.export() for p in self.purchases]
        }
    
    @staticmethod
    def create(data):
        purchases = []
        for p in data["purchases"]:
            purchases.append(Purchase.create(p))
        return Product(data["name"], data["stock"], data["income"], data["id"], purchases)
    

    
class Purchase(object):
    def __init__(self, name=u"", price=0, quantity=0, date=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date = date or dateutils.now()
    
    def export(self):
        return {
            "name": self.name,
            "date": dateutils.totuple(self.date),
            "price": self.price,
            "quantity": self.quantity,
        }
    
    @staticmethod
    def create(data):
        return Purchase(data["name"], data["price"], data["quantity"], dateutils.fromtuple(data["date"]))
