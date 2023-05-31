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

# oath_json = PROJECT_DIR / 'oauth_json/pv_yt_oauth.json'
# yt_manager = YouTubeManger(oath_json)

url = 'https://www.youtube.com/@laogao'
lao_gao_id = get_channel_id_from_url(url)
print(lao_gao_id)

xiao_lin_url = 'https://www.youtube.com/@xiao_lin_shuo'
xiao_lin_id = get_channel_id_from_url(xiao_lin_url)
print(xiao_lin_id)

my_url = 'https://www.youtube.com/@puffvayne5688'
my_id = get_channel_id_from_url(my_url)
print(my_id)




