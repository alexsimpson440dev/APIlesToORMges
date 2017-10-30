import bcrypt
from src.database import Database
from src.user import User

#database manager class
#calls the database
class DBManager():
    def __init__(self):
        self.database = Database()

    #sends user info to the database
    def add_user(self, first_name, last_name, email_address, password):
        hash_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        user = User(first_name, last_name, email_address, password=hash_password)
        self.database.add_user(user)
