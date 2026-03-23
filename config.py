# config.py
# central place for API keys and configs

import os
from dotenv import load_dotenv

load_dotenv()

# API keys loaded from .env
DID_API_KEY = os.getenv("DID_API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# Output path
VOICE_FILE = "outputs/voice.mp3"