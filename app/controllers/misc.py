# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.document import document, set_document
from app.model.document import Document
from app.utils.currency import parsenumber, formatcurrency

import json

def error():
    template_response("/error/error.mako")


def notfound():
    local.response.status_code = 404
    template_response("/error/notfound.mako")


def cashlog():
    log = ((t.date, t.description, t.amount) for t in document().cash_in_hand.transactions)
    template_response("/page/cash_log.mako",
        log = log,
        balance = document().cash_in_hand.get_balance()
    )


def adjust_cash():
    amount = parsenumber(local.request.form.get("amount", u""))

    if amount != None and amount != 0:
        document().cash_in_hand.add_transaction("Justerede kassebeholdning", amount)

        amount_str = formatcurrency(abs(amount))
        if amount < 0:
            document().save("Tog %s fra kassen." % (amount_str,))
        else:
            document().save("Lagde %s i kassen." % (amount_str,))
    redirect("misc.cashlog")


def transfer():
    template_response("/page/transfer.mako")


def import_file():
    data = json.load(local.request.files.get("savefile"))
    new_doc = Document.create(data)
    new_doc.save("Importerede dokument", "savedir/save.beer")
    set_document(new_doc)
    redirect("version.browse")


def enter_title_form():
    template_response("/page/enter_title.mako")


def enter_title_do():
    title = local.request.form.get("title", u"")

    if len(title) == 0:
        return redirect("misc.enter_title_form")

    document().title = title
    document().save(u'Ændrede titel til "%s"' % (title,))

    redirect("index.index")
