# Application to play with Twilio's Text API and AI

This application serves as a template for integrating Twilio's SMS API with OpenAI's GPT model. It allows users to send SMS messages and receive AI-generated responses based on the content of the messages.

## Environment Variables

Make sure to set the following environment variables in your `.env` file:

- `NGROK_AUTH_TOKEN`: Your ngrok authentication token.
- `APPLICATION_PORT`: The port on which the FastAPI application will run (default is 8000).
- `OPENAI_API_KEY`: Your OpenAI API key.
- `TWILIO_API_SID`: Your Twilio API SID.
- `TWILIO_API_SECRET`: Your Twilio API secret.
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
- `PHONE_NUMBER_FROM`: The Twilio phone number you are using to send messages.


## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Launching the Application

1. **Run the FastAPI application:**
   ```bash
   fastapi dev main.py
   ```

2. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000` to see the application running. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.