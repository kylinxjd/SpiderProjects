

# http://pic.ibaotu.com/01/45/84/03C888piCW9D.jpg-0.jpg!ww700

import requests

head = {
    'Referer': 'https://ibaotu.com/tupian/xiaoren/1-1-91647-0-0-0-c0_0-1.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
res = requests.get('https://pic.ibaotu.com/01/50/38/81w888piCCvr.jpg-0.jpg!w340', headers=head)

with open('b.png', 'wb') as f:
    f.write(res.content)
