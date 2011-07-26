# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

from app.controllers import notfound
from app.model.inventory import Product, Purchase

from app.document import inventory, document

from app.utils.currency import parsenumber

def browse():
    products = [(a.id, a.name, a.total_purchase(), a.fixedprice) for a in inventory.list_by_name()]
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
        fixedprice = parsenumber(fixedprice)

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
        fixedprice = parsenumber(fixedprice)

    product = Product(name=name, fixedprice=fixedprice)
    inventory.add_product(product)

    document.save(u"Tilføjede produkt '%s'" % (product.name, ))

    redirect("product.edit", product_id=product.id)

def purchase_form(product_id):
    product = inventory.get_product(product_id)
    template_response("/page/product/purchase_form.mako",
        product_id = product.id,
        product_name = product.name,
    )

def purchase_do(product_id):
    product = inventory.get_product(product_id)

    name = local.request.form.get("name", u"")
    quantity = int(local.request.form.get("quantity", u"0"))
    price = parsenumber(local.request.form.get("price", u"0"))

    purchase = Purchase(name, price, quantity)
    product.add_purchase(purchase)

    document.save(u"Tilføjede indkøb '%s' til '%s'" % (product.name, name))
    redirect("product.edit", product_id=product.id)
