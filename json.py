#importing json
import json
with open("aa.json") as f:
    d = json.load(f,strict=False)
    
    #importing json without strickness
import json
with open("aa.json") as f:
    d = json.load(f)
