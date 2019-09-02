# import csv
# import re
#
# import requests
# from bs4 import BeautifulSoup
#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
# }
#
# res = requests.get(url='http://product.dangdang.com/25312917.html', headers=header)
#
# html = res.text
#
# soup = BeautifulSoup(html, 'html.parser')
#
# obj = soup.select('ul[class="key clearfix"] li')
# obj1 = soup.select('div[class="messbox_info"] span')
# obj2 = soup.select('div[class="sale_box_left"] div[class="name_info"] h1')
# obj3 = soup.select('p[id="dd-price"]')
# dic = {}
# for o in obj:
#     txt = o.get_text().strip()
#     if txt:
#         txt = re.sub(r' ', '', txt)
#         txt_list = txt.split('：')
#         dic[txt_list[0]] = txt_list[1]
# for o in obj1:
#     txt = o.get_text().strip()
#     if re.search(r'\d+条评论', txt):
#         comments = re.search(r'(\d+)条评论', txt).group(1)
#         dic['评论数'] = comments
#     elif re.search(r':', txt):
#         txt_list = txt.split(':')
#         dic[txt_list[0]] = txt_list[1]
#
# dic['书名'] = obj2[0].attrs['title']
# dic['价格'] = obj3[0].get_text().strip().split('¥')[1]
# print(dic)
# data = {
#     "bookName": dic.get('书名', '---'),
#     "author": dic.get('作者', '---'),
#     "publish": dic.get('出版社', '---'),
#     "publishTime": dic.get('出版时间', '---'),
#     "price": dic.get('价格', '---'),
#     "ISBN": dic.get('国际标准书号ISBN', '---'),
#     "comments": dic.get('评论数', '---'),
#     "paperType": dic.get('纸张', '---'),
#     "package": dic.get('包装', '---'),
#     # 是否套装
#     "isSuit": dic.get('是否套装', '---'),
#     "category": dic.get('所属分类', '---'),
# }
# # fieldnames = ['bookName', 'author', 'publish', 'publishTime', 'price', 'ISBN', 'comments', 'paperType', 'package', 'isSuit', 'category']
# # with open('dangdang.csv', 'a+', newline='') as f:
# #     writer = csv.DictWriter(f, fieldnames=fieldnames)
# #     # # 写第一行表头
# #     writer.writeheader()
# #     # # 一次写一行
# #     # writer.writerow({'head1': 'write1', 'head2': 'write2', 'head3': 'write3'})
# #     # 一次写多行
# #     writer.writerows([data, data])
#
# # import pymongo
# #
# # key = 'python'
# # client = pymongo.MongoClient("127.0.0.1", 27017)
# # db = client['dangdang']
# # coll = db[key]
# # coll.insert(doc_or_docs={'name': 'xjj'})
import re
sts = 'asdfnkjcntfsdfjdkslhj'
# (?:com|cn|net)
print(re.match('.*?(com|cn|net).*?', sts).group(1))
