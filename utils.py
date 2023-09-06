from typing import Any
from googleapiclient.discovery import build


def get_youtube_data(api_key: str, channel_ids: list[str]) -> list[dict[str, Any]]:
    """Получение данных о каналах и видео с помощью API YouTube"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    data = []
    for channel_id in channel_ids:
        channel_data = youtube.channels().list(part='snippet, statistics', id=channel_id).execute()
        print(channel_data)


def create_database(database_name: str, params: dict) -> None:
    """Создание базы данных и таблиц для сохранения данных о каналах и видео"""


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict) -> None:
    """Сохранение данных о каналах и видео в базу данных"""
