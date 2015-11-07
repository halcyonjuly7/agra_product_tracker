
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import render_template, redirect, url_for, request
from flask.views import View, MethodView
from flask.ext.login import login_required
################################

### Local Imports ###
from agra.apps.products import products
from agra import lm, mongo
from agra.misc_helper_functions.metaclass import (login_is_required,
                                                  get_categories,
                                                  get_quantities_below_five)

################################


@login_is_required
class Index():

    def get(self):
        collection = mongo.db.products
        categories = get_categories(collection)
        low_quantity_items = get_quantities_below_five(mongo)
        return render_template('/products/index.html',
                               categories=categories,
                               products=low_quantity_items)

    def post(self):
        product = request.form.get('search')
        return redirect(url_for("products_blueprint.Search", product=product))


@login_is_required
class Search():
    def get(self, product):
        collection = mongo.db.products
        searched_product = collection.find({"name":
                                           {'$regex': product,
                                            '$options': "xi"}})
        categories = get_categories(collection)
        return render_template('/products/search.html',
                               products=searched_product,
                               categories=categories)

    def post(self, product):
        product = request.form.get('search')
        return redirect(url_for("products_blueprint.Search", product=product))


@login_is_required
class Details():
    def get(self, category):
        collection = mongo.db.products
        categories = get_categories(collection)
        product_details = mongo.db.products.find({"category": category})
        return render_template('/products/details.html',
                               products=product_details,
                               categories=categories)

    def post(self, category):
        product = request.form.get('search')
        return redirect(url_for("products_blueprint.Search", product=product))


products.add_url_rule('/',
                      view_func=Index.as_view('Index'),
                      methods=['GET', 'POST'])
products.add_url_rule('/details/<category>',
                      view_func=Details.as_view('Details'),
                      methods=['GET', 'POST'])
products.add_url_rule('/search/<product>',
                      view_func=Search.as_view('Search'),
                      methods=['GET', 'POST'])


