from app import db # Import the db instance
from datetime import datetime # Import datetime for timestamps

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Auto-incrementing primary key
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) # Must be unique
    password_hash = db.Column(db.String(128), nullable=False) # Store the hashed password
    target_language = db.Column(db.String(50), nullable=True) # Optional for now
    fluency_level = db.Column(db.String(50), nullable=True) # Optional for now
    conversations = db.relationship('Conversation', backref='user', lazy=True)

    # Add methods for setting and checking password later
    # Example: def set_password(self, password): ...
    # Example: def check_password(self, password): ...

    def __repr__(self):

        return f'<User {self.email}>'



# Models for Scrum-38 (Conversation and Message)
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Link to User table
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Timestamp when conversation started
    topic = db.Column(db.String(100), nullable=True) # Optional: Store the topic
    # Define the relationship to Message (one Conversation has many Messages)
    messages = db.relationship('Message', backref='conversation', lazy=True, cascade="all, delete-orphan") # cascade ensures messages are deleted if conversation is deleted

    def __repr__(self):
        return f'<Conversation {self.id} started by User {self.user_id}>'

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False) # Link to Conversation table
    sender = db.Column(db.String(10), nullable=False) # 'user' or 'ai'
    text = db.Column(db.Text, nullable=False) # The actual message content
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Timestamp when message was sent

    def __repr__(self):
        return f'<Message {self.id} from {self.sender} in Conversation {self.conversation_id}>'