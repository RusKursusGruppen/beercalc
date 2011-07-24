# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.document import accounts
def browse():
    accounts_iter = ((a.id, a.name, a.get_balance()) for a in accounts.list_by_name())
    template_response("/page/account/browse.mako",
        accounts = accounts_iter,
    )

def edit(id):
    account = accounts.get_account(id)
    transactions = account.transactions
    
    transactions = ((t.date, t.description, t.amount)  for t in transactions)
    template_response("/page/account/edit.mako",
        balance = account.get_balance(),
        email = account.email,
        name = account.name,
        transactions = transactions
    )

def create_form():
    account_list = ((x.id, x.name,x.get_balance()) for x in accounts.list_by_name())
    template_response("/page/account/browse.mako",
        account_list = account_list
    )

