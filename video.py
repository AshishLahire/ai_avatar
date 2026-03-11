# video.py

import requests
import time
import config


def create_video(script):

    print("\nStep 4: Requesting avatar video from HeyGen...")

    url = "https://api.heygen.com/v2/video/generate"

    headers = {
        "X-Api-Key": config.HEYGEN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": config.AVATAR_ID
                },
                "voice": {
                    "type": "text",
                    "input_text": script
                }
            }
        ]
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
    except Exception as e:
        print("HeyGen request error:", e)
        return None

    print("HeyGen API response:", data)

    if not data.get("data"):
        print("Video request failed.")
        return None

    video_id = data["data"].get("video_id")

    if not video_id:
        print("Video ID missing from response.")
        return None

    print("Video request successful.")
    print("Video ID:", video_id)

    return video_id


def wait_for_video(video_id):

    print("\nStep 5: Checking video generation status...")

    if not video_id:
        print("No video id received.")
        print("Reason: avatar unavailable OR insufficient credits")
        return None

    url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"

    headers = {
        "X-Api-Key": config.HEYGEN_API_KEY
    }

    while True:

        try:
            response = requests.get(url, headers=headers)
            data = response.json()
        except Exception as e:
            print("Status check error:", e)
            return None

        status = data["data"]["status"]

        print("Video status:", status)

        if status == "completed":
            video_url = data["data"]["video_url"]
            print("Video generated successfully")
            print("Video link:", video_url)
            return video_url

        if status == "failed":

            error = data["data"].get("error")

            print("Video generation failed.")

            if error:
                print("Failure reason:", error.get("message"))

            return None

        time.sleep(6)