from dotenv import load_dotenv
from google import genai
load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents= "What is the capital city of Bangladesh"
)
print(response.text)