from flask import Flask, render_template
from dotenv import load_dotenv
from controllers.chat_controller import ChatController
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)
    
# Initialize controller
chat_controller = ChatController()
    
@app.route('/')
def index():
    chat_controller.ensure_user_session()
    return render_template('chat.html')

@app.route('/create_chat', methods=['POST'])
def create_chat():
    return chat_controller.create_chat()

@app.route('/send_message', methods=['POST'])
def send_message():
    return chat_controller.send_message()

if __name__ == '__main__':
    app.run(debug=True, port=3000) 