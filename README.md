# Application to play with Twilio's Text API and AI

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