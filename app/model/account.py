# -*- coding: utf-8 -*-

from uuid import uuid4
import app.utils.date as dateutils


class Accounts(object):
    def __init__(self, accounts=None):
        self.accounts = accounts or dict()

    def get_balance(self):
        return sum(x.get_balance() for x in self.accounts.itervalues())

    def add_account(self, account):
        self.accounts[account.id] = account

    def exists(self, name, email):
        for a in self.accounts.values():
            if a.name == name and a.email == email:
                return True
        return False

    def get_account(self, id_):
        return self.accounts[id_]

    def list_by_name(self):
        def sortcmp(a, b):
            if a.istutor and not b.istutor:
                return 1
            elif b.istutor and not a.istutor:
                return -1

            return cmp(a.name, b.name)

        ret = self.accounts.values()
        ret.sort(sortcmp)
        return ret

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
