from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



#headless selenium firefox and chrom
https://stackoverflow.com/questions/50414007/unable-to-invoke-firefox-headless

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

element.send_keys(Keys.DOWN) #keys


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

#finding elements 
html_list = self.driver.find_element_by_id("myId")
items = html_list.find_elements_by_tag_name("li")
for item in items:
    text = item.text
    print text




#Handling extensions in browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

coptions = Options()
coptions.add_extension("path/to/extension/file.crx")
driver = webdriver.Chrome(chrome_options=coptions)




#adding proxy to selenium 
proxy = "40.114.121.235"
port = 3128

fp = webdriver.FirefoxProfile()
fp.set_preference('network.proxy.ssl_port', int(port))
fp.set_preference('network.proxy.ssl', proxy)
fp.set_preference('network.proxy.http_port', int(port))
fp.set_preference('network.proxy.http', proxy)
fp.set_preference('network.proxy.type', 1)

browser = webdriver.Firefox(firefox_profile=fp)

#adding proxy from csv

with open("/home/work_aholic/Testing_codes/proxys.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        proxy = i[0]
        port = int(i[1])

        fp = webdriver.FirefoxProfile()
        fp.set_preference('network.proxy.ssl_port', int(port))
        fp.set_preference('network.proxy.ssl', proxy)
        fp.set_preference('network.proxy.http_port', int(port))
        fp.set_preference('network.proxy.http', proxy)
        fp.set_preference('network.proxy.type', 1)

browser = webdriver.Firefox(firefox_profile=fp)
driver = webdriver.Firefox()
driver.set_page_load_timeout(10000)


ActionChains(driver).move_to_element(driver.find_element_by_class_name('select-solution-span')).perform()
driver.execute_script("arguments[0].scrollIntoView(true);", sol_player)

A = driver.execute_script(
     "document.getElementsByClassName('chzn-single').setAttribute('style', 'display:block')")

#best wait in selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
delay = 20
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page']/div[3]/div/div[2]/div[1]/table")))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"
    
    
    
  driver.implicitly_wait(10) #simple wait
#situations were thses guys help me 
#1finding elements
