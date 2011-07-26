# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.model.account import Account

import re
from app.utils.currency import parsenumber

from app.document import accounts, document

def cashlog():
    log = ((t.date, t.description, t.amount) for t in document.cash_in_hand.transactions)
    template_response("/page/cash_log.mako",
        log = log,
        balance = document.cash_in_hand.get_balance()
    )
