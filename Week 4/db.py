
from pymongo import MongoClient

class MongoConnector(object):

    def __init__(self):
        # self.app = app # Necessary when we want our Flask app to use this database class
        # My SCRAM username is `admin` and my password is `password` (currently disabled)
        uri = f"mongodb+srv://admin:password@cluster0-lhrx7.mongodb.net/test?retryWrites=true"
        self.db = MongoClient(uri)


    def insert_user(self, user: dict):
        """Insert a new user into the database."""
        return self.db.app.users.insert_one(user).inserted_id


    def get_user(self, email: str):
        """Get an existing user from the database."""
        return self.db.app.users.find_one({"email": email})


if __name__ == "__main__":
    db = MongoConnector()
    user = {
        "name": "simon",
        "email": "simon.woldemichael@ttu.edu",
        "username": "swoldemi",
        "password": "thisismypassword",
    }
    print(db.insert_user(user))
    print(db.get_user("simon.woldemichael@ttu.edu"))