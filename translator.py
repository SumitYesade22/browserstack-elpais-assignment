import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")


def translate_text(text: str) -> str:
    if not RAPIDAPI_KEY or not RAPIDAPI_HOST:
        print("Missing API credentials")
        return text

    url = f"https://{RAPIDAPI_HOST}/gtranslate"

    payload = {
        "text": text,
        "to": "en",
        "from_lang": "es"
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()

            
            if "translated_text" in data:
                return data["translated_text"]

           
            if isinstance(data, str):
                return data

          
            return str(data)

        else:
            print("Translation API error:", response.status_code)

    except Exception as e:
        print("Translation request failed:", e)

    return text
