from flask_WTF import FlaskForm
from wtform import StringField, SubmitField

class form_list(FlaskForm):
    todo = StringField("What do you want to add to this list? ")
    add = SubmitField("Add!")