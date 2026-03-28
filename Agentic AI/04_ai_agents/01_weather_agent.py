import requests, os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_weather(city: str):
    response = requests.get(f"https://wttr.in/{city.lower()}?format=j1")
    data = response.json()
    current_weather = data.get("current_condition", {})[0].get("temp_C", {})
    return current_weather
