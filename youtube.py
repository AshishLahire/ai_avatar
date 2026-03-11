# youtube.py
# generates youtube video ideas

import random


def get_video_title():

    print("Step 1: Generating YouTube idea...")

    ideas = [
        "Why discipline beats motivation",
        "Consistency is the real superpower",
        "Stop waiting for motivation",
        "Small habits change your life",
        "Success is built daily"
    ]

    title = random.choice(ideas)

    print("Idea selected:", title)

    return title