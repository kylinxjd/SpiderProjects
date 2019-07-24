import requests

url = 'https://img03.sogoucdn.com/app/a/100520093/ca86e620b9e623ff-c90007ca74fdae89-f80d6a5a652e42568b70d0b6b32e60c3.jpg'

res = requests.get(url=url)

if res.status_code == 200:
    data = res.content
    with open('a.jpg', 'wb') as f:
        f.write(data)
