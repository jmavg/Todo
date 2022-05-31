from flask import Flask, request, render_template
from flask_mongoengine import MongoEngine
from forms import form_list_add


app = Flask(__name__)
db = MongoEngine()

app.config["SECRET KEY"] = "mykeytobechanged"
app.config["MONGODB_SETTINGS"] = {'db':"todo" ,'port':6969}

db.init_app(app)

class Entry(db.Document):
    name = db.StringField()
    steps = db.DictField()


@app.route("/")
def index():

    empty = True

    if Entry.objects.count() != 0:
        empty = False

    return render_template("index.html", empty = empty)
    

@app.route("/create_list")
def create():
    form = form_list_add()
    return render_template("create.html",form = form)