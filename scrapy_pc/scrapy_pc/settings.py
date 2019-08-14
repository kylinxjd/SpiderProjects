# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_pc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_pc'

SPIDER_MODULES = ['scrapy_pc.spiders']
NEWSPIDER_MODULE = 'scrapy_pc.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_pc (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 12

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
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
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
]

# PROXIES = [
#     {'ip_port': '127.0.0.1:1253'},
#     {'ip_port': '127.0.0.1:1253', 'userpassword': '235416'}
# ]

PROXIES_my = [
    "HTTPS://120.83.97.122:9999", "HTTPS://1.197.204.180:9999", "HTTP://120.83.107.185:9999",
    "HTTP://114.230.69.86:9999", "HTTPS://117.91.232.47:9999", "HTTPS://27.43.185.62:9999", "HTTP://1.198.72.58:9999",
    "HTTP://1.199.31.109:9999", "HTTP://123.169.34.154:9999", "HTTP://114.230.69.191:9999",
    "HTTPS://223.241.117.134:8010", "HTTP://120.83.104.172:9999", "HTTPS://113.121.22.250:9999",
    "HTTPS://117.91.132.100:9999", "HTTPS://114.230.86.124:9999", "HTTP://220.189.116.83:8888",
    "HTTP://182.34.35.48:9999", "HTTP://27.43.185.183:9999", "HTTPS://180.119.68.103:9999",
    "HTTP://113.121.20.168:9999", "HTTP://113.124.86.225:9999", "HTTP://117.91.130.41:9999", "HTTPS://1.198.73.10:9999",
    "HTTPS://182.34.33.27:9999", "HTTPS://180.119.68.88:9999", "HTTPS://120.83.96.25:9999",
    "HTTPS://182.34.33.222:9999", "HTTPS://1.197.16.111:9999", "HTTP://113.121.21.172:9999",
    "HTTP://123.163.96.44:9999", "HTTPS://180.119.68.42:9999", "HTTPS://112.85.129.168:9999",
    "HTTPS://1.198.73.38:9999", "HTTPS://182.34.35.62:38922", "HTTP://121.233.206.32:9999",
    "HTTP://120.83.104.251:9999", "HTTP://112.85.130.39:9999", "HTTP://115.53.21.163:9999",
    "HTTP://180.119.141.206:9999", "HTTPS://123.169.34.184:21526", "HTTPS://123.169.35.230:808",
    "HTTP://58.253.159.11:9999", "HTTPS://218.91.112.83:9999", "HTTPS://113.121.22.98:9999",
    "HTTPS://183.143.40.134:61234", "HTTPS://115.53.39.63:9999", "HTTPS://121.233.227.153:9999",
    "HTTPS://114.230.69.163:9999", "HTTP://163.204.242.108:9999", "HTTP://180.119.68.20:9999",
    "HTTP://121.233.207.72:9999", "HTTP://121.233.206.185:9999", "HTTP://1.197.204.135:9999",
    "HTTP://1.197.204.165:9999", "HTTPS://42.159.91.248:8080", "HTTP://112.85.175.196:9999",
    "HTTPS://114.217.192.125:9999", "HTTPS://115.223.114.109:8010", "HTTPS://123.145.190.234:8118",
    "HTTPS://59.38.63.110:8118", "HTTPS://60.182.124.10:61234", "HTTPS://124.93.201.59:59618",
    "HTTPS://60.205.229.126:80", "HTTP://1.198.72.66:9999", "HTTPS://112.84.72.184:9999", "HTTPS://120.83.101.170:808",
    "HTTPS://115.219.108.2:8010", "HTTPS://123.245.13.242:8118", "HTTPS://140.207.50.246:51426",
    "HTTP://122.244.143.136:8118", "HTTPS://120.79.147.254:9000", "HTTPS://222.74.237.246:808",
    "HTTPS://106.15.42.179:33543", "HTTPS://117.84.220.26:8118", "HTTP://114.215.139.19:8118",
    "HTTPS://218.76.253.201:61408", "HTTPS://113.110.45.157:61234", "HTTPS://113.120.36.203:9999",
    "HTTP://113.128.25.56:9999", "HTTP://125.81.79.2:8123", "HTTP://122.4.42.125:20147", "HTTP://125.109.196.192:9999",
    "HTTP://113.121.22.170:9999", "HTTP://171.11.178.37:9999", "HTTP://115.221.114.198:9999",
    "HTTP://58.22.177.50:9999", "HTTPS://171.12.112.169:9999", "HTTPS://59.32.37.193:8010",
    "HTTPS://180.119.68.34:9999", "HTTPS://1.197.16.235:9999", "HTTP://120.83.106.99:9999",
    "HTTP://123.163.122.232:9999", "HTTP://182.116.239.113:9999", "HTTPS://180.119.68.97:9999",
    "HTTPS://121.233.207.132:9999", "HTTP://27.43.185.20:9999", "HTTP://120.83.111.15:9999",
    "HTTP://58.253.153.167:9999", "HTTP://182.34.32.255:9999", "HTTP://58.253.158.123:9999"
]
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy_pc.middlewares.ScrapyPcSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_pc.middlewares.RandomHeaders': 543,
    # 'scrapy_pc.middlewares.RandomProxyMiddleware': 543,
    'scrapy_pc.middlewares.ScrapyPcDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapy_pc.pipelines.ScrapyPcPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
