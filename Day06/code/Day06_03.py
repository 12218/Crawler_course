from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.runoob.com/quiz/html-quiz.html')

browser.switch_to_frame('google_esf') # 切换到名为google_esf的frame

time.sleep(3)

browser.close()