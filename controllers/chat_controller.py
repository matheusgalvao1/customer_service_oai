from flask import jsonify, session, request
from services.chat_service import ChatService
import uuid

class ChatController:
    def __init__(self):
        self.chat_service = ChatService()
    
    def ensure_user_session(self):
        """Ensure user has a session ID."""
        if 'user_id' not in session:
            session['user_id'] = str(uuid.uuid4())
        return session['user_id']
    
    def create_chat(self):
        """Handle chat creation request."""
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'Session expired'}), 401
        
        chat_id = self.chat_service.create_chat(user_id)
        return jsonify({
            'chat_id': chat_id,
            'message': 'Chat created successfully'
        })
    
    def send_message(self):
        """Handle message sending request."""
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'Session expired'}), 401
        
        chat_id = request.json.get('chat_id')
        user_message = request.json.get('message')
        
        if not chat_id or not user_message:
            return jsonify({'error': 'Missing chat_id or message'}), 400
            
        ai_response, error = self.chat_service.process_message(user_id, chat_id, user_message)
        
        if error:
            return jsonify({'error': error}), 404 if error == "Chat not found" else 500
            
        return jsonify({
            'message': ai_response
        }) 