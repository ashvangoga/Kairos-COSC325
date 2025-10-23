from app import db # Import the db instance from your main app file

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Auto-incrementing primary key
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) # Must be unique
    password_hash = db.Column(db.String(128), nullable=False) # Store the hashed password
    target_language = db.Column(db.String(50), nullable=True) # Optional for now
    fluency_level = db.Column(db.String(50), nullable=True) # Optional for now

    # Add methods for setting and checking password later
    # Example: def set_password(self, password): ...
    # Example: def check_password(self, password): ...

    def __repr__(self):
        # Useful representation when printing User objects
        return f'<User {self.email}>'