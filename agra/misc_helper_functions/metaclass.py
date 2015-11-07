from flask import request
from flask.ext.login import login_required
from flask.views import MethodView
from bson.objectid import ObjectId


# class Login_Required(type):
#     def __new__(cls, cls_name, bases, cls_dicts):
#         for key, value in cls_dicts.items():
#             if key in ("get", "post"):
#                 cls_dicts.update({key: login_required(value)})
#         return super().__new__(cls, cls_name, bases, cls_dicts)

# def login_is_required(cls):
#     for key, value in vars(cls).items():
#         if key in ("get", "post"):
#             setattr(cls, key, login_required(value))
#     return cls


def login_is_required(cls):
    new_dict = {}
    for key, value in vars(cls).items():
        if key in ("get", "post"):
            new_dict[key] = login_required(value)
        else:
            new_dict[key] = value
    return type(str(cls), (MethodView,), new_dict)


def get_categories(collection):
    categories = set([product['category'] for product in collection.find()])
    return sorted(categories, key=lambda x: x[0].lower())


def get_products(product, db_object=None):
    products = db_object.db.products.find({"name":
                                          {"$regex": product,
                                           "$options": "i"}})
    return products


def update_info(item, mongo_object):
    name_id = request.json.get("id").split("_").pop()
    new_name = request.json.get(item)
    mongo_object.db.products.update({"_id": ObjectId(name_id)},
                                    {"$set": {item: new_name}})


def get_quantities_below_five(mongo_object):
    quantities_below_five = mongo_object.db.products.find({"quantity":
                                                          {"$lte": 5}})
    
    return quantities_below_five


# class Login_Required(type):
#     def __new__(cls, cls_name, bases, cls_dicts):
#         bases = (MethodView,)
#         decorated_class = super().__new__(cls, cls_name, bases, cls_dicts)
#         return decorated_class
    
    
