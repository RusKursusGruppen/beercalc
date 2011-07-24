# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, url_for, redirect

from app.document import accounts
def browse():
    debtors = ((x.id, x.name,x.get_balance()) for x in accounts.list_debtors_by_name())
    creditors = ((x.id, x.name,x.get_balance()) for x in accounts.list_creditors_by_name())
    template_response("/page/account/browse.mako",
        debtors = debtors,
        creditors = creditors
    )

def edit(id):
    account_list = ((x.id, x.name,x.get_balance()) for x in accounts.list_by_name())
    template_response("/page/account/browse.mako",
        account_list = account_list
    )

def create_form():
    account_list = ((x.id, x.name,x.get_balance()) for x in accounts.list_by_name())
    template_response("/page/account/browse.mako",
        account_list = account_list
    )

