# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.model.account import Account

from app.model.document import Document

import json
import re
from app.utils.currency import parsenumber, formatcurrency

from app.document import accounts, document, set_document

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

def export_file():
    local.response.mimetype = "application/octet-stream"
    disp = "attachment; "
    disp += "filename=export.beer; "
    rfc822_date = document().date.strftime("%a, %d %b %Y %H:%M:%S GMT")
    disp += "modification-date: %s" %(rfc822_date,)
    
    local.response.headers.add("Content-Disposition", disp)
    json.dump(document().export(), local.response.stream)
