# -*- coding: utf-8 -*-
u""

from uuid import uuid4
import app.utils.date as dateutils

class Accounts(object):
    def __init__(self, accounts=None):
        self.accounts = accounts or dict()
    
    def get_balance(self):
        return sum(x.get_balance() for x in self.accounts.itervalues())
        
    def add_account(self, account):
        self.accounts[account.id] = account

    def get_account(self, id_):
        return self.accounts[id_]
    
    def list_by_name(self):
        ret = self.accounts.values()
        ret.sort(key=lambda x: x.name)
        return ret
    
    def list_debtors_by_name(self):
        return filter(lambda x: x.get_balance() > 0, self.list_by_name())
    
    def list_creditors_by_name(self):
        return filter(lambda x: x.get_balance() < 0, self.list_by_name())
    
    def export(self):
        return [a.export() for a in self.accounts.values()]
    
    @staticmethod
    def create(data):
        ret = Accounts()
        for a in data:
            ret.add_account(Account.create(a))
        return ret

class Account(object):
    def __init__(self, id_=None, name=u"", email=u"", istutor=False, transactions=None):
        self.id = id_ or unicode(uuid4().hex)
        self.name = name
        self.email = email
        self.istutor = istutor
        self.transactions = transactions or []
    
    def get_balance(self):
        return sum(x.amount for x in self.transactions)
    
    def add_transaction(self, description=u"", amount=0):
        self.transactions.append(Transaction(description=description, amount=amount))
    
    def export(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "istutor": self.istutor,
            "transactions": [t.export() for t in self.transactions]
        }
    
    @staticmethod
    def create(data):
        trans = []
        for t in data["transactions"]:
            trans.append(Transaction.create(t))
        return Account(data["id"], data["name"], data["email"], data["istutor"], trans)
        
    def __repr__(self):
        return "<account id=%s name=%s balance=%s>" % (repr(self.id), repr(self.name), self.get_balance())


class Transaction(object):
    def __init__(self, id_=None, description=u"", date=None, amount=0):
        self.id = id_ or unicode(uuid4().hex)
        self.description = description
        self.date = date or dateutils.now()
        self.amount = amount
        
    def export(self):
        return {
            "id": self.id,
            "description": self.description,
            "date": dateutils.totuple(self.date),
            "amount": self.amount
        }

    @staticmethod
    def create(data):
        return Transaction(data["id"], data["description"], dateutils.fromtuple(data["date"]), data["amount"])


#accounts = Accounts()
#import random
#for i in range(10,30):
#    account = Account(name=unicode(uuid4().hex))
#    for i in range(3,9):
#        account.add_transaction(u"Transaction " + unicode(i), random.randint(-9000,9000))
#    accounts.add_account(account)
#
#import json
#import pprint
#
#accounts_exported = accounts.export()
#accounts_created = Accounts.create(accounts_exported)
#
#for x in accounts, accounts_created:
#    print "-"*50
#    pprint.pprint( x.list_by_name())
#
#pprint.pprint(Accounts.create(accounts.export()).list_creditors_by_name())
