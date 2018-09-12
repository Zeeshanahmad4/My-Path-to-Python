from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv


#Handling mutliple tabs
browser=webdriver.Firefox()
browser.get('http:/google.com')
browser.execute_script("window.open()")
window_after = browser.window_handles[1]
browser.switch_to_window(window_after)
sleep(3)
browser.get('http://bing.com')
window_before = browser.window_handles[0]
browser.switch_to_window(window_before)




#scrolling window
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):
    lastCount = lenOfPage
    sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True
# Scroll down
        for i in range(30):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)


#saving files
urllib.urlretrieve(src, "filename.png")




