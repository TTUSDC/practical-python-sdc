# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, request, render_template, url_for
from flask_login import LoginManager, current_user, login_user, logout_user

from .models import User, LoginForm, RegistrationForm
from .db import MongoConnector, DatabaseException

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

db_connector = MongoConnector(app)

@login_manager.user_loader
def load_user(email):
	try:
		return db_connector.get_user(email)
	except db.DatabaseException:
		return

@app.route("/login", methods=["GET", "POST"])
def login():
    pass


@app.route("/logout")
def logout():
    if current_user.is_authorized:
        logout_user()
        return "User logged out!"
    flash("Please login first.")
    return redirect(url_for("login"))


@app.route("/register")
def register():
    if current_user.is_authorized:
        logout_user()
        return "User logged out!"
    flash("Please login first.")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)