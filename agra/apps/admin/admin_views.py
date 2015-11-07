
from flask import render_template, redirect, url_for, request
from flask.ext.admin import AdminIndexView, expose, BaseView, expose_plugview
from flask.ext.login import current_user, login_required
from flask.views import MethodView
from agra import mongo
from agra.misc_helper_functions.metaclass import (get_categories,
                                                  get_products,
                                                  update_info,
                                                  get_quantities_below_five)


class IndexView(AdminIndexView): ##A

    @expose('/')
    def index(self):
        return super().index()


class ProductsEdit(BaseView):
    @expose("/", methods=["GET", "POST"])
    def index(self):
        if request.method == "GET":
            collection = mongo.db.products
            categories = get_categories(collection)
            low_quantity_items = get_quantities_below_five(mongo)
            return self.render("/admin_templates/admin_products_edit.html",
                               categories=categories,
                               products=low_quantity_items)

        elif request.method == "POST":
            product = request.form.get("search")
            return redirect(url_for('products_edit.search', product=product))

    @expose("/products/<category>", methods=["GET", "POST"])
    def products_category(self, category):
        if request.method == "GET":
            products = mongo.db.products.find({"category": category})
            collection = mongo.db.products
            categories = get_categories(collection)
            return self.render("/admin_templates/admin_products_edit_category.html",
                               products=products,
                               categories=categories)

        elif request.method == "POST":
            product = request.form.get("search")
            return redirect(url_for('products_edit.search', product=product))

    @expose("/search/<product>", methods=["GET", "POST"])
    def search(self, product):
        if request.method == "GET":
            collections = mongo.db.products
            products = get_products(product=product, db_object=mongo)
            categories = get_categories(collections)
            return self.render("/admin_templates/admin_search.html",
                               categories=categories,
                               products=products)

        elif request.method == "POST":
            product = request.form.get("search")
            return redirect(url_for('products_edit.search', product=product))

    @expose("/change_info", methods=["POST"])
    def change_info(self):
        if request.method == "POST":
            if request.json.get("name"):
                update_info("name", mongo)
          
            elif request.json.get("sku"):
                update_info("sku", mongo)
            
            elif request.json.get("quantity"):
                update_info("quantity", mongo)

            return ""







