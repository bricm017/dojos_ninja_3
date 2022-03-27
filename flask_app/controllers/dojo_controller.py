from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

#This route shows all dojos
@app.route("/")
def index():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("index.html", all_dojos = all_dojos)

@app.route("/add", methods = ["POST"])
def add_dojo():
    Dojo.save(request.form)
    return redirect ("/")

#This route shows a single dojo with all ninjas associated
@app.route("/dojo/<int:id>")
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template("dojo.html", dojo = Dojo.get_one_with_ninjas(data))