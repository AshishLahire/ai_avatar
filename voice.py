# voice.py

import requests
import config


def generate_voice(script):

    print("\nStep 3: Generating voice...")

    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

    headers = {
        "xi-api-key": config.ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": script,
        "model_id": "eleven_turbo_v2"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
    except Exception as e:
        print("Voice API connection error:", e)
        return None

    if response.status_code != 200:
        print("Voice generation failed.")
        print("Reason:", response.text)
        return None

    with open(config.VOICE_FILE, "wb") as f:
        f.write(response.content)

    print("Voice generated successfully.")
    print("Saved to:", config.VOICE_FILE)

    return config.VOICE_FILE