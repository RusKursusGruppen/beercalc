# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.document import accounts, inventory, usage, document

def new_form():
    accounts_iter = ((a.id, a.name) for a in accounts().list_by_name())
    products = [(a.id, a.name) for a in inventory().list_by_name()]
    template_response("/page/usage/form.mako",
        accounts = accounts_iter,
        products = products,
    )

def new_form_do():
    for p in inventory().list_by_name():
        try:
            stock = int(local.request.form.get("stock_%s" % (p.id, ), "0"))
        except:
            stock = 0
        p.stock = stock

        for a in accounts().list_by_name():
            try:
                amount = int(local.request.form.get("usage_%s_%s" % (a.id, p.id), "0"))
            except:
                amount = 0
            usage().update(a.id, p.id, amount)

    usage().commit()
    document().save(u"Afregning")

    redirect("account.browse")
