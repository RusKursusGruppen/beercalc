# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.account

endpoints = {
    "account.create_form": app.controllers.account.create_form,
    "account.browse": app.controllers.account.browse,
    "account.edit": app.controllers.account.edit,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/accounts", "account.browse"),
        ("GET", "/account/view/<string:id>", "account.edit"),
        ("GET", "/account/create", "account.create_form"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
