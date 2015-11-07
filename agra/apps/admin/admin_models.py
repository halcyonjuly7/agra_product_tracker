
from .admin_forms import UserForm, ProductForm
from flask_admin.contrib.pymongo import ModelView

class UserModel(ModelView):
    column_list = ("user", "password")
    form = UserForm


class ProductModel(ModelView):
    column_list = ("name", "img_path", "category", "price", "quantity")
    form = ProductForm
