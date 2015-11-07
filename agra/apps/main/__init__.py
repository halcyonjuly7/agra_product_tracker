
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import Blueprint
################################

### Local Imports ###

################################


main = Blueprint('main_blueprint', __name__)
from .views import *

