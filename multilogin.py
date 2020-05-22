As I understand you want to disable pop-up blocker?
Then you can try to add the following line to your app.properties file: chrome.console_arg.disable-popup-blocking=true

You can try to add the following line to your app.properties file:chrome.console_arg.disable-notifications=true




chrome.console_arg.enable-logging=true


get a list of profiles

url = 'https://api.multiloginapp.com/v1/profile/list/?token=4daa08da9421228d92332c35730dcf41f48b7672&mlaVersion=4.5.3&defaultMode=FAKE'
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


