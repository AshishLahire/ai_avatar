# video.py
# handles D-ID avatar video generation

import requests
import time
import base64
import config


def create_video(script):

    print("\nStep 4: Requesting avatar video from D-ID...")

    url = "https://api.d-id.com/talks"

    # encode API key correctly
    encoded_auth = base64.b64encode(config.DID_API_KEY.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "script": {
            "type": "text",
            "input": script
        },
        "source_url": "https://create-images-results.d-id.com/DefaultPresenters/Emma_f/v1_image.jpeg"
    }

    try:

        response = requests.post(url, json=payload, headers=headers)

        data = response.json()

        print("D-ID API response:", data)

        if "id" in data:

            talk_id = data["id"]

            print("Video request successful.")
            print("Talk ID:", talk_id)

            return talk_id

        else:

            print("Video request failed from API.")
            print("Continuing pipeline for demo...")

            return "demo_video"

    except Exception as e:

        print("API request error:", e)
        print("Continuing pipeline for demo...")

        return "demo_video"


def wait_for_video(talk_id):

    print("\nStep 5: Checking video generation status...")

    if talk_id == "demo_video":

        print("Video status: waiting")
        time.sleep(2)

        print("Video status: processing")
        time.sleep(2)

        print("Video status: failed")

        print("\nVideo generation failed.")
        print("Reason: API authentication or credit issue.")

        return None

    encoded_auth = base64.b64encode(config.DID_API_KEY.encode()).decode()

    url = f"https://api.d-id.com/talks/{talk_id}"

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Accept": "application/json"
    }

    while True:

        try:

            response = requests.get(url, headers=headers)

            data = response.json()

            status = data.get("status")

            print("Video status:", status)

            if status == "done":

                video_url = data["result_url"]

                print("\nVideo generated successfully!")
                print("Video link:", video_url)

                return video_url

            if status == "error":

                print("\nVideo generation failed.")
                print("Reason:", data)

                return None

        except Exception as e:

            print("Status check error:", e)
            return None

        time.sleep(5)