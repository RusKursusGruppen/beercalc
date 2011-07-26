# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.account
import app.controllers.usage

endpoints = {
    "account.create_form": app.controllers.account.create_form,
    "account.browse": app.controllers.account.browse,
    "account.edit": app.controllers.account.edit,
    "usage.new_form": app.controllers.usage.new_form,
    "usage.new_form_do": app.controllers.usage.new_form_do,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/accounts", "account.browse"),
        ("GET", "/account/view/<string:id>", "account.edit"),
        ("GET", "/account/create", "account.create_form"),
        ("GET", "/usage/new", "usage.new_form"),
        ("POST", "/usage/new", "usage.new_form_do"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
