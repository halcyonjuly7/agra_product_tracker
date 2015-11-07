
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import render_template, redirect, url_for, request
from flask.views import View, MethodView
from flask.ext.login import login_user
################################

### Local Imports ###
from agra.apps.main import main
from agra import lm, mongo
from .models import User
################################


@lm.user_loader
def load_user(user):
    return User(user)


class Index(MethodView):
    def get(self):
        return render_template('/main/index.html')

    def post(self):
        username = request.form.get("name")
        password = request.form.get("password")
        does_user_exist = mongo.db.users.find_one({"user": username, "password": password})
        if does_user_exist:
            login_user(User(username))
            return redirect(url_for('products_blueprint.Index'))
        return self.get()


main.add_url_rule('/', view_func=Index.as_view('Index'), methods=['GET', 'POST'])
