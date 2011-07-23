# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.account

endpoints = {
    "account.browse": app.controllers.account.browse,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/accounts", "account.browse"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
