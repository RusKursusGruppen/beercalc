# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.model.account import Account

import re
from app.utils.currency import parsenumber

from app.document import accounts, document
def browse():
    accounts_iter = ((a.id, a.name, a.get_balance()) for a in accounts().list_by_name())
    template_response("/page/account/browse.mako",
        accounts = accounts_iter,
    )

def import_form():
    template_response("/page/account/import_form.mako")

def import_do():
    r = re.compile(r'\S+@\S+', re.UNICODE)
    
    for l in local.request.form.get("data", u"").split("\n"):
        m = r.search(l)
        email = m and m.group(0) or u""
        name = " ".join("".join(r.split(l, maxsplit=1)).split())
        if accounts.exists(name, email):
            continue
        account = Account(name=name, email=email)
        accounts().add_account(account)

    document().save("Kontoimport")
    redirect("account.browse")


def edit(id):
    account = accounts().get_account(id)
    transactions = account.transactions
    
    transactions = ((t.date, t.description, t.amount) for t in transactions)
    template_response("/page/account/edit.mako",
        id = id,
        balance = account.get_balance(),
        email = account.email,
        name = account.name,
        istutor = account.istutor,
        transactions = transactions
    )
def edit_do(id):
    istutor = "istutor" in local.request.form
    email = local.request.form.get("email", u"")
    name = local.request.form.get("name", u"")
    
    account = accounts().get_account(id)
    
    account.name = name
    account.email = email
    account.istutor = istutor

    document().save(u'Ændrede data for konto "%s"'  % (name,))

    redirect("account.edit", id=id)


def create_form():
    template_response("/page/account/create.mako")

def create_do():
    istutor = "istutor" in local.request.form
    email = local.request.form.get("email", u"")
    name = local.request.form.get("name", u"")
    
    account = Account(name=name, email=email, istutor=istutor)
    
    accounts().add_account(account)
    
    document().save(u'Oprettede kontoen "%s"' % (name,))
    redirect("account.browse")

def payment(id):
    def fail(msg=u""):
        return redirect("account.edit", id=id)

    amount = local.request.form.get("amount")
    amount = amount and parsenumber(amount)

    if amount == None:
        return fail()

    account = accounts().get_account(id)
    
    if amount < 0:
        account.add_transaction(u"Udbetaling", amount)
        document().cash_in_hand.add_transaction(u'Udbetaling "%s"' % (account.name,), amount)
    else:
        account.add_transaction(u"Indbetaling", amount)
        document().cash_in_hand.add_transaction(u'Indbetaling "%s"' % (account.name,), amount)
    

    document().save(u'Ind-/udbetaling på konto "%s"' % (account.name,))
    return redirect("account.edit", id=id)
    template_response("/page/test.mako", test=amount)
