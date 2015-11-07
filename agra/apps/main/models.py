
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask.ext.login import UserMixin
################################

### Local Imports ###

################################


class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username
