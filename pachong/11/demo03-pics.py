"""
爬取页面的所有图片地址
按照地址发送请求爬取图片保存
"""
import re
import random
from time import sleep
from urllib.parse import quote
import requests


def getpic(url, directory, header):
    user_agent_list = header
    res = requests.get(url=url, headers={'User-Agent': user_agent_list[0]})

    if res.status_code == 200:
        html = res.text
        # print(html)
        # <img src="" attr="56613" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=6244351eb94543a9f54ef2ce2e27a6bb/f982d143ad4bd113a2ad5cd854afa40f4afb058b.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=5d094a34fe1f3a295ac8d5c6a91ebd31/a686c9177f3e67091860ae1535c79f3df9dc55fc.jpg" class="threadlist_pic j_m_pic "  />
        purl = '<img src="" attr="\d+" data-original=".*?"  bpic="(.*?)" class="threadlist_pic j_m_pic "  />'

        ret = re.findall(purl, html)
        for imgurl in ret:
            img = requests.get(imgurl, headers={'User-Agent': user_agent_list[random.randint(0, 10)]}).content
            imgname = imgurl.split('/')[-1]
            with open(directory + imgname, 'wb') as f:
                f.write(img)
                print(imgname)
                sleep(random.randint(30, 50) // 100)


if __name__ == '__main__':
    # http://tieba.baidu.com/f?kw=%E5%A4%B4%E5%83%8F&ie=utf-8&pn=0
    proxy_list = []
    # 关键词
    keywords = "皮卡丘"
    # 保存目录
    directory_path = 'touxiang/'
    # 对关键词编码
    unicode_keywords = quote(keywords)

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    for i in range(0, 2):
        html_url = 'http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s' % (unicode_keywords, i * 50)
        print(html_url)
        getpic(url=html_url, directory=directory_path, header=user_agent_list)
