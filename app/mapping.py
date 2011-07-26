# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.account
import app.controllers.usage
import app.controllers.product

endpoints = {
    "account.create_form": app.controllers.account.create_form,
    "account.create_do": app.controllers.account.create_do,
    "account.browse": app.controllers.account.browse,
    "account.import": app.controllers.account.import_form,
    "account.import_do": app.controllers.account.import_do,
    "account.edit": app.controllers.account.edit,
    "account.payment": app.controllers.account.payment,
    "account.edit_do": app.controllers.account.edit_do,
    "usage.new_form": app.controllers.usage.new_form,
    "usage.new_form_do": app.controllers.usage.new_form_do,
    "product.browse": app.controllers.product.browse,
    "product.edit": app.controllers.product.edit,
    "product.edit_do": app.controllers.product.edit_do,
    "product.purchase": app.controllers.product.purchase_form,
    "product.purchase_do": app.controllers.product.purchase_do,
    "product.create_form": app.controllers.product.create_form,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/accounts", "account.browse"),
        ("GET", "/accounts/import", "account.import"),
        ("POST", "/accounts/import", "account.import_do"),
        ("GET", "/account/edit/<string:id>", "account.edit"),
        ("GET", "/account/create", "account.create_form"),
        ("POST", "/account/create/do", "account.create_do"),
        ("POST", "/account/edit/do/<string:id>", "account.edit_do"),
        ("POST", "/account/payment/<string:id>", "account.payment"),
        ("GET", "/usage/new", "usage.new_form"),
        ("POST", "/usage/new", "usage.new_form_do"),
        ("GET", "/products", "product.browse"),
        ("GET", "/product/edit/<string:product_id>", "product.edit"),
        ("POST", "/product/edit/<string:product_id>", "product.edit_do"),
        ("GET", "/product/purchase/<string:product_id>", "product.purchase"),
        ("POST", "/product/purchase/<string:product_id>", "product.purchase_do"),
        ("GET", "/product/create", "product.create_form"),
        ("POST", "/product/create", "product.create_do"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
