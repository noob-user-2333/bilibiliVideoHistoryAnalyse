import ast
import time
import requests
import CookiesManage
import VideoHistory
import WatchedVideo


def GetBilibiliVideoHistory(max_pages=100):
    cookieses = CookiesManage.GetCookies('.bilibili.com')
    cookie = CookiesManage.CookiesToRequestsFormat(cookieses)
    url = "https://api.bilibili.com/x/web-interface/history/cursor"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.bilibili.com"
    }

    all_videos = []
    params = {"ps": 20}  # 每页20条
    page = 0

    while page < max_pages:
        response = requests.get(url, cookies=cookie, headers=headers, params=params)
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            break
        json_data = response.json()
        VideoHistory.VideoHistory.create(pageId = page,json = json_data)
        data = json_data.get("data", {})
        videos = data.get("list", [])
        #单独提取视频相关信息并插入sqlite
        for video in videos:
            WatchedVideo.WatchedVideo.create(title=video['title'], bvid=video['history']['bvid'],
                                             author_name=video['author_name'], tag_name=video['tag_name'])
        all_videos.extend(videos)

        params = data.get('cursor',{})
        if (params.get('max') == 0
                or params.get('ps') == 0)\
                or params.get('view_at') == 0:  # 已无更多数据
            break  # 无更多数据

        # 更新下一页的参数（使用最后一条记录的时间戳）
        last_video = videos[-1]
        params["view_at"] = last_video["view_at"]  # 关键分页参数


        page += 1
        time.sleep(1)  # 避免高频请求
    return all_videos
