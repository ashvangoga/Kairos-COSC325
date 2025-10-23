from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # Database instance
bcrypt = Bcrypt(app) # Password hashing instance

# Import models *after* db is created to avoid circular imports
# We will add routes (endpoints) later

if __name__ == '__main__':
    # This allows you to run the app directly using 'python app.py'
    app.run(debug=True) # debug=True helps during development