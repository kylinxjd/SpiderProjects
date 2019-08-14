
from time import sleep

from selenium import webdriver

# 创建一个Chrome的实例
driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
frame = driver.find_element_by_id('login_frame')
driver.switch_to.frame(frame)

sleep(5)
user = driver.find_element_by_id('u')
user.send_keys('762741385@qq.com')
print(user)
sleep(2)
pwd = driver.find_element_by_id('p')
pwd.send_keys('19960824Xjd')
print(pwd)

sleep(2)


driver.find_element_by_id('login_button').click()

cookie = driver.get_cookies()
print(cookie)

# driver.quit()
