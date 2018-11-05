# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, request, render_template, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from login_project.models import User
from login_project.db import MongoConnector

app = Flask(__name__)
app.secret_key = "somethingsecret"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

db_connection = MongoConnector(app)


@login_manager.user_loader
def load_user(email):
    entry = db_connection.get_user(email)
    if entry is not None:
        if request.form["password"] == entry["password"]:
            return User(entry["name"], entry["email"])
    return
   
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entry = db_connection.get_user(request.form["email"])
        if entry is not None:
            if request.form["password"] == entry["password"]:
                user = User(entry["name"], entry["email"])
                login_user(user)
                return "You logged in"
            flash("Incorrect username or password. Please try again.")
            return redirect(url_for("login"))
        flash(f"Unable to find account with email {request.form['email']}")
        return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "You are logged out."


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered.")
        return redirect(url_for("index"))    
    if request.method == "POST":
        print(dict(request.form))
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)