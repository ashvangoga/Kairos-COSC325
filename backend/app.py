from flask import Flask, jsonify, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import openai
import os
from datetime import datetime  # <-- BUG FIX 1: Import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

# --- This completes SCRUM-36 ---
try:
    openai.api_type = "azure"
    openai.api_base = app.config['AZURE_OPENAI_ENDPOINT']
    openai.api_version = "2023-05-15"
    openai.api_key = app.config['AZURE_OPENAI_KEY']
    print("✅ OpenAI client configured for Azure successfully.")
except Exception as e:
    print(f"❌ FAILED to configure OpenAI client for Azure: {e}")
# --- End of SCRUM-36 code ---


# --- BUG FIX 2: Import your new models ---
from models import User, Conversation, Message 

@app.route('/')
def index():
    return "Hello, Pickle Inc. Backend is running!"

# --- THIS IS YOUR NEW API ENDPOINT FOR STEP 3 ---
@app.route('/api/chat/message', methods=['POST'])
def process_message():
    data = request.get_json()
    user_id = data.get('userId')
    conversation_id = data.get('conversationId')
    user_text = data.get('text')

    # ... (Your backend logic will go here) ...
    
    print(f"Received from FE: {data}")
    mock_ai_text = "This is a mock AI response. The backend logic is not built yet."
    
    response_json = {
        "conversationId": conversation_id or 1,
        "aiResponse": {
            "sender": "ai",
            "text": mock_ai_text,
            "timestamp": datetime.utcnow().isoformat()
        },
        "userMessage": {
            "sender": "user",
            "text": user_text,
            "timestamp": datetime.utcnow().isoformat()
        }
    }
    
    return jsonify(response_json), 200