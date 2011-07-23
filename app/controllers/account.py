# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, url_for, redirect

import app.model.document as document

def browse():
    template_response("/page/index.mako",
        russer=russer,
        page=page,
        pagecount = pagecount
    )

