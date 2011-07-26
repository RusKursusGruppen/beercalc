# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.account
import app.controllers.usage
import app.controllers.product

endpoints = {
    "account.create_form": app.controllers.account.create_form,
    "account.browse": app.controllers.account.browse,
    "account.edit": app.controllers.account.edit,
    "usage.new_form": app.controllers.usage.new_form,
    "usage.new_form_do": app.controllers.usage.new_form_do,
    "product.browse": app.controllers.product.browse,
    "product.view": app.controllers.product.view,
    "product.create_form": app.controllers.product.create_form,
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
        ("GET", "/products", "product.browse"),
        ("GET", "/product/view/<string:product_id>", "product.view"),
        ("GET", "/product/create", "product.create_form"),
        ("POST", "/product/create", "product.create_do"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
