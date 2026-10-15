
from dotenv import load_dotenv
import os
import time
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

start = time.perf_counter()

print("Sending request to Gemini...")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Reply with just the word Hello."
)

end = time.perf_counter()

print("Response:", response.text)
print("Total time:", round(end - start, 2), "seconds")
