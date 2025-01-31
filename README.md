# Cover Letter Assistant Chat

A web-based chat application that acts as a personal assistant for job seekers. It uses your cover letter to answer questions from recruiters in a personalized way, powered by OpenAI's API.

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   python app.py
   ```
   The application will be available at http://localhost:3000

## API Endpoints

- `GET /` - Main chat interface
- `POST /create_chat` - Create a new chat session
- `POST /send_message` - Send a message and get AI response

## Notes

- The application uses Flask's built-in development server. For production, use a proper WSGI server like Gunicorn
- Make sure to keep your OpenAI API key secure and never commit it to version control
- The chat history is currently stored in memory; consider implementing persistent storage for production use 