
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import Blueprint
################################

### Local Imports ###

################################


products = Blueprint('products_blueprint', __name__)
from .views import *

