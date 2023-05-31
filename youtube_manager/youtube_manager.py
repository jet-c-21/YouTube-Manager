# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 5/31/23
"""
import pathlib
from typing import Union, List

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from .playlist import Playlist


class YouTubeManger:
    SCOPES = [
        'https://www.googleapis.com/auth/youtube.force-ssl'
    ]
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'

    def __init__(self, oauth_json_path: Union[pathlib.Path, str]):
        self.oauth_json_path = pathlib.Path(oauth_json_path)
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            str(self.oauth_json_path), self.SCOPES
        )
        flow.run_local_server()
        self.yt_api = googleapiclient.discovery.build(
            serviceName=self.API_SERVICE_NAME,
            version=self.API_VERSION,
            credentials=flow.credentials
        )

        msg = f"YouTube API {self.API_VERSION} initialized"
        print(msg)

    def get_my_playlists(self) -> List:
        playlists = list()
        page_token = None

        while True:
            request = self.yt_api.playlists().list(
                part='snippet,contentDetails,id,status',
                maxResults=50,
                mine=True,
                pageToken=page_token
            )
            response = request.execute()

            # print(response)
            for data in response['items']:
                playlists.append(Playlist(data, self.yt_api))

            # playlists.append(Playlist(response['items']))

            page_token = response.get('nextPageToken')
            if not page_token:
                break

        return playlists

    def create_playlist(self, playlist_title: str, privacy_status: str = 'public', description='') -> Playlist:
        body = {
            'snippet': {
                'title': playlist_title,
                'description': description,  # optional, add description if needed
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }

        request = self.yt_api.playlists().insert(
            part='snippet,status',
            body=body
        )
        response = request.execute()

        return Playlist(response, self.yt_api)

    def get_playlist(self, playlist_id: str) -> Playlist:
        request = self.yt_api.playlists().list(
            part='snippet,contentDetails,id,status',
            maxResults=1,
            id=playlist_id
        )
        response = request.execute()
        items = response.get('items')

        if not items:
            raise ValueError(f'Playlist with ID {playlist_id} not found')
        else:
            return Playlist(items[0], self.yt_api)