# -*- coding: utf-8 -*-
from app.document import document
import app.utils.misc


def doc_title():
    return document().title


def timedelta(date):
    return app.utils.misc.template_render('/widget/timedelta.mako', date=date)

