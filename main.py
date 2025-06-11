import ast
from time import sleep

from peewee import fn

import VideoHistory
import VideoInfo
import WatchedVideo
import requests

from GetBilibiliVideoHistory import GetBilibiliVideoHistory


def get_video_tags(bvid):
    url = f"https://api.bilibili.com/x/web-interface/view/detail/tag?bvid={bvid}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": f"https://www.bilibili.com/video/{bvid}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data.get("code") == 0:
            tags = [(tag["tag_name"],tag['tag_id']) for tag in data.get("data", [])]
            return tags
        else:
            print("API返回错误:", data.get("message"))
    else:
        print("请求失败，状态码:", response.status_code)
    return []


if __name__ == "__main__":
    GetBilibiliVideoHistory(10000)
    videos = WatchedVideo.WatchedVideo.select().where(fn.length(WatchedVideo.WatchedVideo.bvid) > 0)
    for video in videos:
        bvid = video.bvid
        tags = get_video_tags(bvid)
        for tag_name, tag_id in tags:
            VideoInfo.VideoInfo.create(bvid=bvid, tag_id=tag_id, tag_name=tag_name)
            sleep(0.5)
        print("视频标签:", tags)