import os
from google import genai
from dotenv import load_dotenv

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Initialize the client (it automatically detects GEMINI_API_KEY from the environment)
client = genai.Client()

# 3. Generate content using the Gemini model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello! Explain how to use Gemini in Python briefly.",
)

print(response.text)