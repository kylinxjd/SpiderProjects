import requests

url = 'https://www.cnblogs.com/TurboWay/p/8172246.html'

res = requests.get(url=url)

if res.status_code == 200:
    print('请求成功')
    print(res.encoding)
