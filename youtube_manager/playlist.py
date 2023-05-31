# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 5/31/23
"""
from typing import Dict

"""
{
    "kind": "youtube#playlist",
    "etag": "LG3fWuX9Vx0uRAVJADajahbp1LE",
    "id": "PLqSgX1Zu_6lyy35TQz1UXvqOSZvwpAAwk",
    "snippet": {
        "publishedAt": "2023-02-05T07:37:23Z",
        "channelId": "UC8dEtTVE8qsQwVwuRa2IAOg",
        "title": "Study with BTS",
        "description": "",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/gq6DfoS-l9A/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/gq6DfoS-l9A/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/gq6DfoS-l9A/hqdefault.jpg",
                "width": 480,
                "height": 360
            },
            "standard": {
                "url": "https://i.ytimg.com/vi/gq6DfoS-l9A/sddefault.jpg",
                "width": 640,
                "height": 480
            },
            "maxres": {
                "url": "https://i.ytimg.com/vi/gq6DfoS-l9A/maxresdefault.jpg",
                "width": 1280,
                "height": 720
            }
        },
        "channelTitle": "Puff Vayne",
        "localized": {
            "title": "Study with BTS",
            "description": ""
        }
    },
    "status": {
        "privacyStatus": "public"
    },
    "contentDetails": {
        "itemCount": 1
    }
}
"""
import datetime


class Playlist:
    def __init__(self, data: Dict, yt_api):
        self.id = data.get('id')
        self.title = data.get('snippet').get('title')
        self.publish = datetime.datetime.strptime(data.get('snippet').get('publishedAt'), "%Y-%m-%dT%H:%M:%SZ")
        self.description = data.get('snippet').get('description')
        self.channel_id = data.get('snippet').get('channelId')
        self.channel_title = data.get('snippet').get('channelTitle')
        self.privacy_status = data.get('status').get('privacyStatus')
        self._yt_api = yt_api
        self._video_ls = None

    def __repr__(self):
        s = f"<Playlist - {self.title} - {self.id}>"
        return s

    def delete(self):
        request = self._yt_api.playlists().delete(id=self.id)
        response = request.execute()
        if response == '':
            return True
        return response

    @property
    def video_ls(self):
        if self._video_ls is not None:
            return self._video_ls

        video_ls = list()
        page_token = None

        while True:
            request = self._yt_api.playlistItems().list(
                part='snippet',
                maxResults=50,
                playlistId=self.id,
                pageToken=page_token
            )
            response = request.execute()

            for item in response['items']:
                video_id = item['snippet']['resourceId']['videoId']
                video_ls.append(video_id)

            page_token = response.get('nextPageToken')
            if not page_token:
                break

        self._video_ls = video_ls
        return self._video_ls