from typing import Dict, List, Optional

class ChatManager:
    def __init__(self):
        self.chats: Dict[str, Dict[str, Dict]] = {}  # user_id -> chat_id -> chat_data
    
    def create_chat(self, user_id: str, chat_id: str, cover_letter: str) -> None:
        """Create a new chat for a user."""
        if user_id not in self.chats:
            self.chats[user_id] = {}
        
        self.chats[user_id][chat_id] = {
            'cover_letter': cover_letter,
            'messages': []
        }
    
    def get_chat(self, user_id: str, chat_id: str) -> Optional[Dict]:
        """Get a chat by user_id and chat_id."""
        return self.chats.get(user_id, {}).get(chat_id)
    
    def add_message(self, user_id: str, chat_id: str, role: str, content: str) -> None:
        """Add a message to a chat."""
        if chat := self.get_chat(user_id, chat_id):
            chat['messages'].append({"role": role, "content": content})
    
    def get_conversation(self, user_id: str, chat_id: str) -> List[Dict]:
        """Get the full conversation including system message."""
        if chat := self.get_chat(user_id, chat_id):
            return [
                {"role": "system", "content": f"You are a personal assistant helping recruiters learn about a candidate. Use the following cover letter as context for your responses: {chat['cover_letter']}"}
            ] + chat['messages']
        return [] 