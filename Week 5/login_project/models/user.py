# -*- coding: utf-8 -*-

from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_id(self):
        return self.email