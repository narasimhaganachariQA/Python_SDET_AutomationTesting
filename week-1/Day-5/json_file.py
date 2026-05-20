import json

with open("jsonData.json",'r') as file:
    data=json.load(file)

for user in data:
    if user["version"]>5.1:
        print("Name :", user["name"])
        print("ID:",user["id"])
        print("Language: ",user["language"])
        print("Version :",user["version"])