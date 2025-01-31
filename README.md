# Cover Letter Assistant Chat

A web-based chat application that acts as a personal assistant for job seekers. It uses your cover letter to answer questions from recruiters in a personalized way.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Features

- Create new chat sessions
- Upload your cover letter as context
- Interactive chat interface
- Persistent chat history
- Modern and responsive UI 