import requests
import re
import time
def images():
    for i in range(1,10):
        # 获取网页
        url = f'http://www.win4000.com/wallpaper_detail_58939_{i}.html'
        # 请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            'cookie':'UM_distinctid=178348b2545a8-088ac5ff19a43a-1f241205-1fa400-178348b2546577; t=1952259f914e3a43916739cbd1107597; r=151; XSRF-TOKEN=eyJpdiI6ImRlZkJ6c2ZWSWVZN0ZqTU1JSVdrbGc9PSIsInZhbHVlIjoiQUNMekN2ODUrUnhMejYyQ1lGMVpCdHErQ2hPQnl1bVB3OFBneVRQU09zMGpVdUx1YXhwaWFzVUtXXC9QVkVMaVVMTzFDbHBpejVlOWlFZUpTdHowSjlnQnJnc3h2UVJTNjFsRmZFdDVFbkMwQnpLblU2K0IrWkQ5VWkxd1M5SDNkIiwibWFjIjoiZDFjMTYzN2Y1ZjRlNzRkMTUwM2ZkNDUyMGQ3MTI4NTA0MTkzNzQyZjcwMzI4YzhiY2ZjZDhlNmNhY2I1ZTRkMCJ9; win4000_session=eyJpdiI6ImMrQ2M0QU9uYmJvbDdFS29uOVdYS2c9PSIsInZhbHVlIjoibVRWaHZmbU9NXC9XaGNWWHh4S3IyNkpKaVBRQmY3ODIrMndsR0ErY0c1MnhSbXZ5TStJY0R4SmZhOTJxYm9VeDZoYTJUZjhUTXpyd0N0UlVVU1hQYzdkRW1ya0R4aGM4cWZvTGdaSk5CVnk2bzVQK3FzQ2tuTUYzZEwwcWZOZnAwIiwibWFjIjoiNWYxMjU2MTUyYjUyMmE4YzllYWYxYWYyNTJkYWYzODU3YTUwZDJlZmUwZjc2YmE1NWFkNjg0NzNmYzRjZTBjOCJ9; CNZZDATA1279564249=994225968-1615784110-https%3A%2F%2Fwww.baidu.com%2F|1615897544'
        }
        # 发送请求
        response = requests.get(url,headers=headers)
        data = response.content.decode('utf-8')
        # print(data)
        partten = re.compile('<img class="pic-large" src="(.*)" alt="好玩经典游戏刺客信条高清炫酷个性图片桌面壁纸下载第二辑" title="好玩经典游戏刺客信条高清炫酷个性图片桌面壁纸下载第二辑"/>')
        result = partten.findall(data)
        # print(result)
        for img in result:
            print(img)
            f = requests.get(img)
            # print(f)
            time.sleep(1)
            with open(f'images/tupian{i}.jpg','wb') as code:
                code.write(f.content)
images()