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

sample_user = {
    "name": "Simon Woldemichael",
    "email": "simon.woldemichael@ttu.edu",
    "password": "password",
}

@login_manager.user_loader
def load_user(email):
    if email == sample_user["email"]:
        return User(sample_user["name"], sample_user["email"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    print(current_user.is_anonymous)
    if current_user.is_anonymous:
        if request.method == "POST":
            if request.form["password"] == sample_user["password"]:
                user = User(sample_user["name"], sample_user["email"])
                login_user(user)
                return "You logged in!"
            print("Incorrect password. Please try again.")
            return redirect(url_for("login"))
        return render_template("login.html")
    return "You are already logged in!"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "You are logged out."


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        print("You are already registered.")
        return redirect(url_for("index"))    
    if request.method == "POST":
        # What would you do to extract and use this form data?
        print(request.form) 
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)