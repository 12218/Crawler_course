from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://taobao.com')

input_target = browser.find_element_by_class_name('search-combobox-input')
print(input_target)

input_tag = browser.find_elements_by_class_name('search-combobox-input')
print(input_tag)

browser.close()

