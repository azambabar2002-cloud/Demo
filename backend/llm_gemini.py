from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()  # reads GEMINI_API_KEY

resp = client.models.generate_content(
    model="gemini-3.8-flash",  # check AI Studio for the current model name
    contents="Write anything in 2 sentences",
)
print(resp.text)