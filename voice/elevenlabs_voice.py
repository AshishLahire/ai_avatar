import requests
import config

def generate_voice(script):

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{config.VOICE_ID}"

    headers = {
        "xi-api-key": config.ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": script,
        "model_id": "eleven_monolingual_v1"
    }

    response = requests.post(url, json=data, headers=headers)

    with open(config.OUTPUT_AUDIO, "wb") as f:
        f.write(response.content)

    print("Voice generated:", config.OUTPUT_AUDIO)