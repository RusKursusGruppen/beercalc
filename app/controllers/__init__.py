# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local


def error():
    template_response("/error/error.mako")

def notfound():
    template_response("/error/notfound.mako")
