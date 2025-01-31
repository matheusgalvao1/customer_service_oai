import requests
import time

def run_conversation_test():
    # Start a new chat
    print("\n=== Starting New Chat Session ===\n")
    response = requests.post('http://localhost:5000/create_chat')
    if response.status_code != 200:
        print("Error creating chat!")
        return
    
    chat_id = response.json()['chat_id']
    
    # List of questions to test different aspects of the cover letter
    questions = [
        "What's your name and current position?",
        "Can you tell me about your most recent project at TechCorp Solutions?",
        "How did you improve the API performance using Redis?",
        "What kind of experience do you have with cloud technologies?",
        "Tell me about a challenging problem you solved at DataFlow Systems.",
        "What programming languages are you most comfortable with?",
        "How many people are in your current team and what's your leadership style?",
        "What made you transition from StartupTech to DataFlow Systems?",
        "Can you elaborate on your experience with React and frontend development?",
        "What certifications do you hold and when did you obtain them?"
    ]
    
    print("Starting conversation...\n")
    print("-" * 80)
    
    for i, question in enumerate(questions, 1):
        print(f"\nQ{i}: {question}")
        
        # Send message and get response
        response = requests.post(
            'http://localhost:5000/send_message',
            json={
                'chat_id': chat_id,
                'message': question
            }
        )
        
        if response.status_code == 200:
            answer = response.json()['message']
            print(f"\nA: {answer}")
            print("\n" + "-" * 80)
        else:
            print(f"Error getting response: {response.status_code}")
        
        # Small delay to avoid overwhelming the API
        time.sleep(1)

if __name__ == "__main__":
    print("Make sure the Flask application is running on http://localhost:5000")
    print("Starting conversation test in 3 seconds...")
    time.sleep(3)
    run_conversation_test() 