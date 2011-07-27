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
    
    def remove_product(self, id):
        del self.products[id]
    
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
    def __init__(self, name=u"", stock=0, income=None, id_=None, purchases=None, fixedprice=None, profit=None):
        self.purchases = purchases or {}
        self.name = name
        self.stock = stock
        self.income = income or Account()
        self.profit = profit or Account()
        self.id = id_ or unicode(uuid4().hex)
        self.fixedprice = fixedprice
    
    def add_purchase(self, product):
        self.products[product.id] = product
    
    def list_purchases_by_date(self):
        ret = self.purchases.values()
        ret.sort(key=lambda x: x.date)
        return ret
    
    def add_purchase(self, purchase):
        self.purchases[purchase.id] = purchase
    
    def get_purchase(self, id):
        return self.purchases[id]
    
    def remove_purchase(self, id):
        del self.purchases[id]

    def total_purchase(self):
        return sum(x.price for x in self.purchases.values())
    
    def total_quantity(self):
        return sum(x.quantity for x in self.purchases.values())
    
    def value_left(self):
        return (self.total_purchase() * self.stock) / self.total_quantity()
    
    def add_profit(self, amount):
        self.profit.add_transaction("Added profit", amount)

    def get_price(self, sold_individual, sold_total):
        missing_income = self.total_purchase()
        missing_income += self.profit.get_balance()
        missing_income -= self.income.get_balance() + self.value_left()

        return (sold_individual * missing_income) / sold_total
    
    def get_fixedprice(self, count=0):
        if self.fixedprice is None:
            return (self.total_purchase() * count) / self.total_quantity()
        else:
            return count * self.fixedprice
    
    def export(self):
        return {
            "id": self.id,
            "name": self.name,
            "fixedprice": self.fixedprice,
            "stock": self.stock,
            "income": self.income.export(),
            "profit": self.profit.export(),
            "purchases": [p.export() for p in self.purchases.values()]
        }
    
    @staticmethod
    def create(data):
        product = Product(
            name = data["name"],
            stock = data["stock"],
            income = Account.create(data["income"]),
            profit = Account.create(data["profit"]),
            id_ = data["id"],
            purchases = [],
            fixedprice = data["fixedprice"]
        )
        for p in data["purchases"]:
           product.add_purchase(Purchase.create(p))
        return product
    
class Purchase(object):
    def __init__(self, name=u"", price=0, quantity=0, date=None, id=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date = date or dateutils.now()
        self.id = id or unicode(uuid4().hex)
    
    def export(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": dateutils.totuple(self.date),
            "price": self.price,
            "quantity": self.quantity,
        }
    
    @staticmethod
    def create(data):
        return Purchase(
            name = data["name"],
            price = data["price"],
            quantity = data["quantity"],
            date=dateutils.fromtuple(data["date"]),
            id = data["id"]
        )
