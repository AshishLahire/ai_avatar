from scraper.youtube_scraper import scrape_youtube_titles
from script.script_generator import generate_script
from voice.elevenlabs_voice import generate_voice
from video.heygen_video import create_video, check_status, download_video


def run_pipeline():

    print("Step 1: Scraping YouTube titles...")
    titles = scrape_youtube_titles()

    print("Step 2: Generating script...")
    script = generate_script(titles)

    print(script)

    print("Step 3: Generating voice...")
    generate_voice(script)

    print("Step 4: Creating HeyGen avatar video...")
    video_id = create_video(script)

    print("Step 5: Checking video status...")
    video_url = check_status(video_id)

    print("Step 6: Downloading final video...")
    download_video(video_url)


if __name__ == "__main__":
    run_pipeline()