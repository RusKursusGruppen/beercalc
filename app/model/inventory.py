# -*- coding: utf-8 -*-
from uuid import uuid4
import app.utils.date as dateutils
from app.model.account import Account

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
    def __init__(self, name=u"", stock=0, income=None, id_=None, purchases=None):
        self.purchases = purchases or []
        self.name = name
        self.stock = stock
        self.income = income or Account()
        self.id = id_ or unicode(uuid4().hex)
    
    def add_purchase(self, purchase):
        self.purchases.append(purchase)

    def total_purchase(self):
        return sum(x.price for x in self.purchases)
    
    def total_quantity(self):
        return sum(x.quantity for x in self.purchases)
    
    def value_left(self):
        return (self.total_purchase() * self.stock) / self.total_quantity()

    def get_price(self, sold_individual, sold_total):
        missing_income = self.total_purchase() - self.income.get_balance() - self.value_left()
        return (sold_individual * missing_income) / sold_total
    
    def get_fixedprice(self, count=0, price=None):
        if price is None:
            return (self.total_purchase() * count) / self.get_quantity()
        else:
            return count * price
    
    def export(self):
        return {
            "id": self.id,
            "name": self.name,
            "stock": self.stock,
            "income": self.income.export(),
            "purchases": [p.export() for p in self.purchases]
        }
    
    @staticmethod
    def create(data):
        purchases = []
        return Product(
            name = data["name"],
            stock = data["stock"],
            income = Account.create(data["income"]),
            id_ = data["id"],
            purchases = [Purchase.create(p) for p in data["purchases"]]
        )
    
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
