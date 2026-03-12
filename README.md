# AI Avatar Video Generator

This project is a simple AI automation pipeline that generates a short motivational video using multiple AI services.

The system performs the following steps automatically:

1. Generate a YouTube video idea
2. Generate a motivational script
3. Convert the script to voice
4. Send the script to HeyGen to generate an avatar video
5. Check the video generation status and print the final result

Even if the video generation fails (for example due to insufficient credits), the system continues and shows the reason for failure.

---

## Project Workflow

The pipeline runs in the following sequence:

Step 1 → Generate YouTube Idea

Step 2 → Generate Script

Step 3 → Generate Voice

Step 4 → Request Avatar Video (HeyGen API)

Step 5 → Check Video Status


Example output:

```
Step 1: Generating YouTube idea
Idea selected: Stop waiting for motivation

Step 2: Generating script prompt
Prompt used:
Write a short motivational YouTube shorts script for the title: Stop waiting for motivation

Step 3: Generating voice
Voice generated successfully

Step 4: Requesting avatar video from HeyGen
Video request successful
Video ID: xxxxxxxxx

Step 5: Checking video generation status
Video status: waiting
Video status: failed

Reason: Insufficient HeyGen credits

