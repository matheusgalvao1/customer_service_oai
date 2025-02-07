from models.chat import ChatManager
from openai import OpenAI
from typing import Dict, Optional, Tuple
import os
import uuid

class ChatService:
    def __init__(self):
        self.chat_manager = ChatManager()
        self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.system_prompt = self._load_system_prompt()
    
    def _load_system_prompt(self) -> str:
        """Load the system prompt from file."""
        try:
            with open('data/system_prompt.txt', 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Error loading system prompt: {e}")
            return "You are a helpful assistant."
    
    def create_chat(self, user_id: str) -> str:
        """Create a new chat session."""
        chat_id = str(uuid.uuid4())
        self.chat_manager.create_chat(user_id, chat_id, self.system_prompt)
        return chat_id
    
    def process_message(self, user_id: str, chat_id: str, message: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Process a user message and get AI response.
        Returns: Tuple of (ai_response, error_message)
        """
        chat = self.chat_manager.get_chat(user_id, chat_id)
        if not chat:
            return None, "Chat not found"
        
        # Add user message
        self.chat_manager.add_message(user_id, chat_id, "user", message)
        
        try:
            # Get AI response
            conversation = self.chat_manager.get_conversation(user_id, chat_id)
            
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                temperature=0.7,
                max_tokens=500
            )
            
            ai_message = response.choices[0].message.content
            
            # Add AI response to chat history
            self.chat_manager.add_message(user_id, chat_id, "assistant", ai_message)
            
            return ai_message, None
            
        except Exception as e:
            return None, f"Error getting AI response: {str(e)}"
    
    def get_chat(self, user_id: str, chat_id: str) -> Optional[Dict]:
        """Get chat data."""
        return self.chat_manager.get_chat(user_id, chat_id) 