import requests
import json

url = "https://smart-reminder-web-app-ztisgbssmq-el.a.run.app/schedule"

response = requests.get(url).json()
# print(response)

data = json.dumps(response, indent=4)
with open("data.json", "w") as f:
    f.write(data)

