import requests
from bs4 import BeautifulSoup

def scrape_youtube_titles():

    url = "https://www.youtube.com/@aliabdaal/videos"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []

    for link in soup.find_all("a"):
        title = link.get("title")
        if title:
            titles.append(title)

    return titles[:5]