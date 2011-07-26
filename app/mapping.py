# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.account

endpoints = {
    "account.create_form": app.controllers.account.create_form,
    "account.create_do": app.controllers.account.create_do,
    "account.browse": app.controllers.account.browse,
    "account.edit": app.controllers.account.edit,
    "account.edit_do": app.controllers.account.edit_do,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/accounts", "account.browse"),
        ("GET", "/account/edit/<string:id>", "account.edit"),
        ("GET", "/account/create", "account.create_form"),
        ("POST", "/account/create/do", "account.create_do"),
        ("POST", "/account/edit/do/<string:id>", "account.edit_do"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
