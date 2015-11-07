
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField, FileField, HiddenField, StringField
################################

### Local Imports ###

################################


class UserForm(Form):
    username = TextField("username")
    password = PasswordField("password")

class ProductForm(Form):
    category = TextField("category")
    name = TextField("name")
    price = TextField("price")
    quantity = TextField("quantity")
    image_path = TextField("image_path")



