
### Standard Library Imports ###

################################

### 3rd Party Imports ###

#################################

### Local Imports ###
from agra import create_app, admin, mongo
from agra.apps.admin.admin_models import *
from agra.apps.admin.admin_views import ProductsEdit
#################################

if __name__ == "__main__":
    app = create_app("config")
    with app.app_context():
        admin.add_view(UserModel(mongo.db.users, endpoint='users'))
        admin.add_view(ProductModel(mongo.db.products, endpoint="products"))
        admin.add_view(ProductsEdit(name="Edit Products",
                                    endpoint="products_edit"))

    app.run()
