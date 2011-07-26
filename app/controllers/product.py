# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.controllers import notfound

from app.document import inventory

def browse():
    products = [(a.id, a.name, a.stock) for a in inventory.list_by_name()]
    template_response("/page/product/browse.mako",
        products = products,
    )

def view(product_id):
    try:
        product = inventory.get_product(product_id)
    except KeyError:
        notfound()
        return

    template_response("/page/test.mako", test=product.export())

def create_form():
    pass

def create_do():
    pass

