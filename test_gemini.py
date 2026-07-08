from google import genai

def read_api_key():
    with open(".env", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                return line.split("=", 1)[1].strip()

    return None


api_key = read_api_key()

print("API Key Found:", api_key is not None)

if api_key is None:
    raise ValueError("API key not found in .env")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Introduce yourself in two lines."
)

print(response.text)