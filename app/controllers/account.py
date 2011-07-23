# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, url_for, redirect

from app.document import accounts
def browse():
    template_response("/page/account/browse.mako",
        test = accounts.list_by_name()
    )

