# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

def faq():
    template_response("/page/help/faq.mako")
