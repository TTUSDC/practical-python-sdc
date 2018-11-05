
from pymongo import MongoClient

class MongoConnector(object):

    def __init__(self, app):
        self.app = app
        uri = f"mongodb+srv://admin:password6969@cluster0-lhrx7.mongodb.net/test?retryWrites=true"
        self.db = MongoClient(uri)


    def insert_user(self, user: dict):
        with self.app.app_context():
            return self.db.app.users.insert_one(user).inserted_id


    def get_user(self, email: str):
            return self.db.app.users.find_one({"email": email})


if __name__ == "__main__":
    db = MongoConnector(None)
    user = {
        "name": "simon",
        "email": "simon.woldemichael@ttu.edu",
        "username": "swoldemi",
        "password": "password",
    }
    print(db.insert_user(user))
    print(db.get_user("simon.woldemichael@ttu.edu"))