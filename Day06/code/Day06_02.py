from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://taobao.com')
input_tag = browser.find_elements_by_class_name('search-combobox-input')[0] # 寻找到淘宝输入框
print(input_tag)
input_tag.send_keys('Python') # 在输入框输入Python
time.sleep(3)
input_tag.clear() # 清除输入框的文字
input_tag.send_keys('JavaScript') # 在输入框输入JavaScript

button = browser.find_elements_by_class_name('btn-search')[0] # 寻找淘宝的搜索按钮
print(button)
button.click() # 点击按钮
time.sleep(3)
browser.close() # 关闭浏览器