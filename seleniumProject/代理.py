
from selenium import webdriver
import random
ip_pool = []

with open('ip.txt', 'r') as f:
    ip = f.readline().strip()
    while ip:
        ip_pool.append(ip)
        ip = f.readline().strip()

print(ip_pool)

chromeOptions = webdriver.ChromeOptions()

# 设置代理
chromeOptions.add_argument("--proxy-server=http://123.163.96.123:9999")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152 61.135.155.82:443
browser = webdriver.Chrome(chrome_options=chromeOptions)

# 查看本机ip，查看代理是否起作用
browser.get("http://httpbin.org/ip")

# 退出，清除浏览器缓存
# browser.quit()

