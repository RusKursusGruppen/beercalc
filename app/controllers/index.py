# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.model.account import Account

import re
from app.utils.currency import parsenumber

from app.document import accounts, document, inventory



def index():
    cash_in_hand = document().cash_in_hand.get_balance()
    

    recievable_cash = 0
    for a in accounts().accounts.values():
        b = a.get_balance()
        if b < 0:
            recievable_cash += abs(b)
    
    income = 0
    expenses = 0
    for p in inventory().products.values():
        expenses += p.total_purchase()
        income += p.income.get_balance()

    template_response("/page/index.mako",
        comment = document().comment,
        date = document().date,
        income = income,
        expenses = expenses,
        recievable_cash = recievable_cash,
        cash_in_hand = cash_in_hand

    )

