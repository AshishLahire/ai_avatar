# main.py

import os

from youtube import get_video_title
from script import generate_script
from voice import generate_voice
from video import create_video, wait_for_video


def run():

    os.makedirs("outputs", exist_ok=True)

    title = get_video_title()

    script = generate_script(title)

    generate_voice(script)

    video_id = create_video(script)

    wait_for_video(video_id)


if __name__ == "__main__":
    run()