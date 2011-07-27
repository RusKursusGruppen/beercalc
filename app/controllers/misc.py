# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.model.account import Account

import re
from app.utils.currency import parsenumber, formatcurrency

from app.document import accounts, document

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
