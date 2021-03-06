# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.model.document import Document
from app.document import set_document

import os
import json


def browse():
    files = []
    for f in filter(lambda x: x != '.placeholder', os.listdir('savedir')):
        doc = Document.load("savedir/" + f)
        files.append((f, doc.date, doc.comment))

    files.sort(key=lambda x: x[1], reverse=True)

    template_response("/page/version/browse.mako",
        files=files
    )


def view(filename):
    doc = Document.load("savedir/" + filename)
    template_response("/page/version/view.mako",
        filename=filename,
        date=doc.date,
        comment=doc.comment
    )


def rollback(filename):
    doc = Document.load("savedir/" + filename)
    doc.save("Rullede tilbage til version '%s'"
            % (filename.replace("save.beer.", ""), ), "savedir/save.beer")

    set_document(doc)

    redirect("version.browse")


def export(filename):
    doc = Document.load("savedir/" + filename)
    local.response.mimetype = "application/octet-stream"
    disp = "attachment; "
    disp += "filename=export.beer; "
    rfc822_date = doc.date.strftime("%a, %d %b %Y %H:%M:%S GMT")
    disp += "modification-date: %s" % (rfc822_date,)

    local.response.headers.add("Content-Disposition", disp)
    json.dump(doc.export(), local.response.stream)
