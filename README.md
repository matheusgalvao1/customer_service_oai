# TechCare Solutions Customer Service Chat

A web-based chat application that provides automated customer service for TechCare Solutions. The chat bot uses company information to answer questions about services, pricing, support options, and more, powered by OpenAI's API.

## Features

- Real-time chat interface
- Automated responses based on company information
- Quick-access buttons for common queries
- Professional and friendly AI customer service representative
- Support for multiple chat sessions

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

## Project Structure

- `data/company_info.txt` - Contains company information, services, pricing, and policies
- `data/system_prompt.txt` - Defines the AI's behavior and response guidelines
- `templates/chat.html` - The chat interface template
- `services/chat_service.py` - Core chat processing logic
- `models/chat.py` - Chat data management
- `controllers/chat_controller.py` - Request handling and routing

## API Endpoints

- `GET /` - Main chat interface
- `POST /create_chat` - Create a new chat session
- `POST /send_message` - Send a message and get AI response

## Customization

To adapt this for your own company:
1. Update `data/company_info.txt` with your company's information
2. Modify `data/system_prompt.txt` to adjust the AI's behavior
3. Customize the chat interface in `templates/chat.html`
4. Adjust the suggested prompts to match your common customer queries