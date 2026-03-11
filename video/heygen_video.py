import requests
import time
import config

def create_video(script):

    url = "https://api.heygen.com/v2/video/generate"

    headers = {
        "X-Api-Key": config.HEYGEN_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
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

    response = requests.post(url, json=data, headers=headers)

    result = response.json()

    print("HeyGen Response:", result)

    video_id = result["data"]["video_id"]

    return video_id


def check_status(video_id):

    url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"

    headers = {
        "X-Api-Key": config.HEYGEN_API_KEY
    }

    while True:

        response = requests.get(url, headers=headers)
        data = response.json()

        status = data["data"]["status"]

        print("Video status:", status)

        if status == "completed":
            return data["data"]["video_url"]

        time.sleep(10)


def download_video(video_url):

    response = requests.get(video_url)

    with open(config.OUTPUT_VIDEO, "wb") as f:
        f.write(response.content)

    print("Final video saved:", config.OUTPUT_VIDEO)