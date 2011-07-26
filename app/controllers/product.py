# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.controllers import notfound
from app.model.inventory import Product

from app.document import inventory, document

def browse():
    products = [(a.id, a.name, a.stock) for a in inventory.list_by_name()]
    template_response("/page/product/browse.mako",
        products = products,
    )

def edit(product_id):
    try:
        product = inventory.get_product(product_id)
    except KeyError:
        notfound()
        return

    purchases_iter = ((p.name, p.price, p.quantity, p.date) for p in product.purchases)

    template_response("/page/product/edit.mako",
        id = product.id,
        name = product.name,
        stock = product.stock,
        fixedprice = product.fixedprice,
        purchases = purchases_iter
    )

def edit_do(product_id):
    name = local.request.form.get("name", u"")
    fixedprice = local.request.form.get("fixedprice", u"")
    if len(fixedprice) == 0:
        fixedprice = None
    else:
        fixedprice = int(fixedprice)

    product = inventory.get_product(product_id)

    product.name = name
    product.fixedprice = fixedprice

    document.save(u"Ændrede data for produkt '%s'" % (name,))

    redirect("product.edit", product_id=product_id)

def create_form():
    template_response("/page/product/create.mako")

def create_do():
    name = local.request.form.get("name", u"")
    fixedprice = local.request.form.get("fixedprice", u"")
    if len(fixedprice) == 0:
        fixedprice = None
    else:
        fixedprice = int(fixedprice)

    product = Product(name=name, fixedprice=fixedprice)
    inventory.add_product(product)

    document.save(u"Tilføjede produkt '%s'" % (product.name, ))

    redirect("product.browse")

def purchase_form():
    pass

def purchase_do():
    pass
