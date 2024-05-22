import requests
from bs4 import BeautifulSoup


def get_videos():
    URL = "https://www.youtube.com/feed/trending"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    video_divs = soup.find_all("div", class_="ytd-video-renderer")

    videos = []

    for video_div in video_divs:
        title = video_div.find("a", id="video-title").text.strip()
        channel = video_div.find(
            "a", class_="yt-simple-endpoint style-scope yt-formatted-string"
        ).text.strip()
        videos.append({"title": title, "channel": channel})

    return videos
