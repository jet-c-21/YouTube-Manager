# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 5/31/23
"""
import sys
import pathlib

# add project directory to path
curr_file_path = pathlib.Path(__file__).absolute()
PROJECT_DIR = curr_file_path.parent.parent
sys.path.append(str(PROJECT_DIR))
print(f"[INFO] - append directory to path: {PROJECT_DIR}")

from youtube_manager import YouTubeManger
from youtube_manager.tool import get_channel_id_from_url
from tqdm.auto import tqdm

oath_json = PROJECT_DIR / 'oauth_json/pv_yt_oauth.json'
yt_manager = YouTubeManger(oath_json)

channel_url = 'https://www.youtube.com/@xiao_lin_shuo'
channel_id = get_channel_id_from_url(channel_url)
print(f"channel id = {channel_id}")

# use yt_manager.yt_api to get all video ids
channel_video_id_ls = []
page_token = None

while True:
    request = yt_manager.yt_api.search().list(
        part="id",
        channelId=channel_id,
        maxResults=50,
        pageToken=page_token,
        type='video'
    )
    response = request.execute()

    for item in response['items']:
        video_id = item['id']['videoId']
        channel_video_id_ls.append(video_id)

    page_token = response.get('nextPageToken')
    if not page_token:
        break

print(f"channel videos count = {len(channel_video_id_ls)}")

# then use yt_manager.yt_api to add all videos into the playlist
playlist_id = 'PLqSgX1Zu_6ly-Cq9EljZI-6XeqBPiZzaN'

for video_id in tqdm(channel_video_id_ls):
    request_body = {
        'snippet': {
            'playlistId': playlist_id,
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video_id
            }
        }
    }

    request = yt_manager.yt_api.playlistItems().insert(
        part='snippet',
        body=request_body
    )
    response = request.execute()
