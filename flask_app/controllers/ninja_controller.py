from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/add/ninja", methods=["POST"])
def add_ninja():
    Ninja.add_new_ninja(request.form)
    return redirect("/")


@app.route("/new/ninja")
def new_ninja():
    return render_template("ninja.html", dojos = Dojo.get_all())