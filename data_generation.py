from faker import Faker
from faker.providers import BaseProvider
import csv
import random


class VideoResolutionProvider(BaseProvider):
    def video_resolution(self):
        resolutions = [
            "720x480",
            "1280x720",
            "1920x1080",
            "3840x2160",
        ]
        return self.random_element(resolutions)


genres = [
    "Action",
    "Adventure",
    "Animation",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Family",
    "Fantasy",
    "History",
    "Horror",
    "Music",
    "Mystery",
    "Romance",
    "Science Fiction",
    "Thriller",
    "War",
    "Western",
]


last_position = 0
faker = Faker()
faker.add_provider(VideoResolutionProvider)


def generate_analytics() -> tuple:
    return (
        faker.pyint(0, 100000),
        faker.pydecimal(min_value=0, max_value=1),
        faker.pydecimal(min_value=0, max_value=1),
    )


def generate_metadata() -> tuple:
    return (
        faker.file_extension(category="video"),
        faker.video_resolution(),
        faker.pyint(8000, 48000),
        faker.pyint(3, 10),
    )


def generate_video() -> tuple:
    return (
        faker.text(256),
        faker.text(50),
        faker.date_time_between(start_date="-5y", end_date="now"),
        faker.pyint(1, 100000),
        faker.pyint(0, 2),
        None,
        None,
        faker.pyint(1, 36000),
    )


def generate_user() -> tuple:
    return (
        faker.pyint(0, 2),
        str(faker.pyint(0, 100000)) + faker.user_name(),
        faker.password(64),
        str(faker.pyint(0, 100000)) + faker.email(),
    )


def generate_playlist() -> tuple:
    return (
        faker.text(64),
        faker.date_time_between(start_date="-5y", end_date="now"),
        faker.pyint(1, 36000),
    )


def generate_comment() -> tuple:
    return (faker.text(1000), faker.date())


def generate_genre() -> str:
    return genres.pop()


def generate_user_video(video_qty, user_qty) -> tuple:
    return (faker.pyint(1, user_qty), faker.pyint(1, video_qty))


def generate_user_playlist(user_qty, playlist_qty) -> tuple:
    return (faker.pyint(1, user_qty), faker.pyint(1, playlist_qty))


def generate_video_genre(video_qty, genre_qty) -> tuple:
    return (faker.pyint(1, video_qty), faker.pyint(1, genre_qty))


def generate_video_playlist(video_qty, playlist_qty) -> tuple:
    return (faker.pyint(1, video_qty), faker.pyint(1, playlist_qty))


def generate_user_comment(user_qty, comment_qty) -> tuple:
    return (faker.pyint(1, user_qty), faker.pyint(1, comment_qty))


def generate_video_comment(video_qty, comment_qty) -> tuple:
    return (faker.pyint(1, video_qty), faker.pyint(1, comment_qty))
