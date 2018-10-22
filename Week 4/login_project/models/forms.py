# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm #, RecaptchaField
from wtforms import StringField, validators


class LoginForm(FlaskForm):
    """Encapsulation of a form for questions asked by the student."""
    username = StringField("username", [validators.DataRequired()])
    password = StringField("password", [validators.DataRequired()])
    # recaptcha = RecaptchaField()


class RegistrationForm(FlaskForm):
    email = StringField("email", [validators.DataRequired()])
    email_confirm = StringField("email_confirm", [validators.DataRequired()])
    password = StringField("password", [validators.DataRequired()])
    password_confirm = StringField("password_confirm", [validators.DataRequired()])
    # recaptcha = RecaptchaField()