# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.controllers.misc import notfound
from app.model.account import Account
from app.document import accounts, document
from app.utils.currency import parsenumber

import re


def browse():
    accounts_iter = ((a.id, a.name, a.get_balance()) for a in accounts().list_by_name())
    template_response("/page/account/browse.mako",
        accounts = accounts_iter,
    )


def import_form():
    template_response("/page/account/import_form.mako")


def import_do():
    r = re.compile(r'\S+@\S+', re.UNICODE)

    count = 0
    for l in local.request.form.get("data", u"").split("\n"):
        m = r.search(l)
        email = m and m.group(0) or u""
        name = " ".join("".join(r.split(l, maxsplit=1)).split())

        if name == u"" and email == u"":
            continue
        if accounts().exists(name, email):
            continue

        count += 1
        account = Account(name=name, email=email)
        accounts().add_account(account)

    if count == 1:
        document().save("Kontoimport (%d konto)" % (count,))
    else:
        document().save("Kontoimport (%d konti)" % (count,))

    redirect("account.browse")


def edit(id):
    try:
        account = accounts().get_account(id)
    except KeyError:
        return notfound()
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
    try:
        account = accounts().get_account(id)
    except KeyError:
        return notfound()

    istutor = "istutor" in local.request.form
    email = local.request.form.get("email", u"")
    name = local.request.form.get("name", u"")

    account.name = name
    account.email = email
    account.istutor = istutor

    document().save(u'Ændrede data for konto "%s"' % (name,))

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

    try:
        account = accounts().get_account(id)
    except KeyError:
        return notfound()

    amount = local.request.form.get("amount")
    amount = amount and parsenumber(amount)

    if amount == None:
        return fail()

    if amount < 0:
        account.add_transaction(u"Udbetaling", amount)
        document().cash_in_hand.add_transaction(u'Udbetaling "%s"' % (account.name,), amount)
    else:
        account.add_transaction(u"Indbetaling", amount)
        document().cash_in_hand.add_transaction(u'Indbetaling "%s"' % (account.name,), amount)

    document().save(u'Ind-/udbetaling på konto "%s"' % (account.name,))
    return redirect("account.edit", id=id)
