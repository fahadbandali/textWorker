from dotenv import load_dotenv
import os
from fastapi import Depends, FastAPI, Response, BackgroundTasks, Form
from contextlib import asynccontextmanager
import ngrok
import uvicorn
from twilio.rest import Client
from openAIClient import OpenAIClientWrapper


environment = os.getenv("ENVIRONMENT", "development")

load_dotenv(f".env.{environment}")

NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN", "Missing")
APPLICATION_PORT = int(os.getenv("APPLICATION_PORT", 8000))

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Setting up Ngrok Tunnel")
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    listener = await ngrok.forward(addr=APPLICATION_PORT)
    print("Ngrok url", listener.url())
    yield
    print("Tearing Down Ngrok Tunnel")
    ngrok.disconnect()
    
# OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "Missing")
def get_open_ai_client() -> OpenAIClientWrapper:
    return OpenAIClientWrapper(api_Key=OPENAI_API_KEY)

# Twilio Client
TWILIO_API_SID = os.getenv("TWILIO_API_SID", "Missing")
TWILIO_API_SECRET = os.getenv("TWILIO_API_SECRET", "Missing")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "Missing")

PHONE_NUMBER_FROM = os.getenv("PHONE_NUMBER_FROM", "Missing")

def get_twilio_client() -> Client:
    twilio_client = Client(username=TWILIO_API_SID,password=TWILIO_API_SECRET,account_sid=TWILIO_ACCOUNT_SID)
    return twilio_client

# Server related
app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/receive")
def receive(background_tasks: BackgroundTasks, From: str = Form(), Body: str = Form(), open_ai_client: OpenAIClientWrapper = Depends(get_open_ai_client), twilio_client: Client = Depends(get_twilio_client)):
    background_tasks.add_task(send_sms, Body, From, open_ai_client, twilio_client)
    
    return Response(status_code=202)

async def send_sms(message: str, sender: str, open_ai_client: OpenAIClientWrapper, twilio_client: Client):
    try:
        generated_reply = await open_ai_client.prompt(message)
        twilio_client.messages.create(from_=PHONE_NUMBER_FROM,
                        to=sender,
                        body=generated_reply["response"])
    except Exception as e:
        print(f"Error sending SMS: {e}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=APPLICATION_PORT, reload=True)
    