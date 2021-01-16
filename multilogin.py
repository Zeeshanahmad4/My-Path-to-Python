As I understand you want to disable pop-up blocker?
Then you can try to add the following line to your app.properties file: chrome.console_arg.disable-popup-blocking=true

You can try to add the following line to your app.properties file:chrome.console_arg.disable-notifications=true




chrome.console_arg.enable-logging=true


get a list of profiles

url = 'http://localhost.multiloginapp.com:35000/api/v2/profile'
header = {"content-type": "application/json"}
i = 0
while i < 6:
    response = requests.get(url, headers=header)
    try:
        text = json.loads(response.text)
        print(text)
        break
    except:
        time.sleep(5)
        i = i + 1
        
        
c = -1
d = 1
for restaurant in text['data']:
    c += d
    print (str(c) + "," +   "1" + "," + restaurant['sid']+ "," +restaurant['name'] +  ","  +   "22/05/2020" + ","    "0"  + "," + "0")



# Deleting thr ids    
alist=[]
response = requests.get("http://localhost.multiloginapp.com:35000/api/v2/profile")
response = json.loads(response.content)
for i in response:
    alist.append(i["uuid"])
    
from time import sleep
for i in alist:
    response = requests.delete(url="http://localhost.multiloginapp.com:35000/api/v2/profile/{}".format(i))    
    print(response)
