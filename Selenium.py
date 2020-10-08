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



#chrome profile in selenium 
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\3amigos\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(executable_path=r"C:\Users\3amigos\Desktop\SourceCode\chromedriver.exe" ,chrome_options=options)





# Mobile emulator
https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation
  
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
browser.close()
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
https://stackoverflow.com/questions/35641019/how-do-you-use-credentials-saved-by-the-browser-in-auto-login-script-in-python-2#comment58968197_35641449

https://stackoverflow.com/questions/15058462/how-to-save-and-load-cookies-using-python-selenium-webdriver

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



#iterating through elemnets who does not have link s

post_elems = browser.find_elements_by_xpath("//*[@id='video-title']")
print len(post_elems)
for i in post_elems:
    i.click()
    sleep(5)
    browser.back()
    sleep(5)
    
    
#getting url of current tab 
print browser.current_url


#adding a profile into firefox
https://stackoverflow.com/questions/50321278/how-to-load-firefox-profile-with-python-selenium
    
    
    
    
#hidden elements that gives null values
    html = browser.page_source
    soup = BeautifulSoup(html)
    divTag = soup.find_all("yt-formatted-string", {"class": "style-scope ytd-toggle-button-renderer style-text"})
    for tag in divTag:
        print tag.text
 #second approch   # for tag in soup.find_all('yt-formatted-string'):
    #     print tag.text

    
    #Selenium firefox rotating proxies 
    import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from bs4 import BeautifulSoup
import lxml
import csv
from itertools import cycle


#-------------------------------------------------------------------------------------------------------------------


def mozilla_change_proxy(browser,proxy):
    
    
    print("Changing to :" + proxy)
    browser.get("about:config")
    
    browser.find_element_by_id("warningButton").click()
    proxy, port = str(proxy).split(":")
    setup_script = (
            'var prefs = Components.classes["@mozilla.org/preferences-service;1"].getService(Compone'
            'nts.interfaces.nsIPrefBranch);prefs.setIntPref("network.proxy.type", 1);'
            'prefs.setCharPref("network.proxy.http", "' + proxy + '");prefs.setIntPref("network.proxy.http_port", "'
            + port + '");prefs.setCharPref("network.proxy.ssl", "' + proxy + '");prefs.setIntPref'
            '("network.proxy.ssl_port", "' + port + '");prefs.setCharPref("network.proxy.ftp", "' + proxy + '");'
            'prefs.setIntPref("network.proxy.ftp_port", "' + port + '");')
    browser.execute_script(setup_script)
    sleep(1)


#-------------------------------------------------------------------------------------------------------------------


def get_fresh_proxies():
    driver=webdriver.Firefox()
    driver.get("https://free-proxy-list.net")
    select=driver.find_element_by_xpath('//div[@id="proxylisttable_length"]//select')
    Select(select).select_by_value('80')

    proxies=[]
    for page in range(4):  
        pages=driver.find_elements_by_xpath('//div[@id="proxylisttable_paginate"]//ul/li/a')
        for i in (0,1,-1,-2):
            pages.pop(i)
        pages[page].click()
        sleep(3)
        soup=BeautifulSoup(driver.page_source,'lxml')
        trs=soup.table.tbody.find_all('tr')
        proxies.extend([tr.td.text+':'+tr.td.next_sibling.text for tr in trs if tr.find('td',class_='hx').text=='yes'])
    driver.close()

    valid_proxies=set()

    for proxy in proxies:
        try:
            #-------------------timeout modified----------
            res=requests.get("https://httpbin.org/ip",proxies={"https":proxy,"http":proxy})
            print("Worked!")
            valid_proxies.add(proxy)

        except:
            print("Nope!")
    return valid_proxies

#-------------------------------------------------------------------------------------------------------------------



def test_proxy(browser):
    try:
        print("running test proxy try ")
        browser.get("https://wtfismyip.com")
        return True
    except:
        print("running test proxy except ")
        return False
    
#-------------------------------------------------------------------------------------------------------------------


# Add coockies and get coockies
from selenium import webdriver
import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def runme():

    driver = webdriver.Chrome()
    driver.get('https://www.slader.com/home/')
    input()
    Cookies = driver.get_cookies()
#     Cookies[f"{email}:{pswd}"]=cookies
    with open("sladerCookies.json", 'w') as file:
        json.dump(Cookies, file)
    return driver


# runme()


# driver = runme()
def runme1():

    driver = webdriver.Chrome()
    driver.get('https://www.slader.com/home/')

    with open('sladerCookies.json') as file:
        cookies = json.load(file)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get('https://www.slader.com/home/')
    return driver


runme1()
input()

