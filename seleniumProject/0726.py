from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 创建一个Chrome的实例
driver = webdriver.Chrome()
driver.get("https://www.sogou.com/")

# elem = driver.find_element_by_xpath('//a[@id="pic"]')
# 填写搜索关键词
elem = driver.find_element_by_id("query")
elem.send_keys('煎蛋')
# 点击搜索按钮
btn = driver.find_element_by_id('stb')
btn.click()
# ActionChains(driver).move_to_element(btn).perform()

# 保存截图
# driver.save_screenshot('a.png')

# html = driver.page_source

# 获取煎蛋官网链接并点击进入
sleep(1)
driver.find_element_by_id('sogou_vr_30000701_0').click()

for i in driver.window_handles:
    print(i)

driver.switch_to.window('CDwindow-B97088BA57ED93D70F388177EF61182E')

# driver.quit()
