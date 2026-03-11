# config.py
# central place for API keys and configs

import os
from dotenv import load_dotenv

load_dotenv()

HEYGEN_API_KEY = os.getenv("HEYGEN_API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# default avatar
AVATAR_ID = "anna_public"

# output path
VOICE_FILE = "outputs/voice.mp3"