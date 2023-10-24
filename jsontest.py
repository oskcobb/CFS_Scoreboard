import json
import requests

r = requests.get('https://raw.githubusercontent.com/oskcobb/CFS_Scoreboard-Themes/main/themes.json')
j = json.loads(r.text)
for num in j["themes"]:
    num = num["name"]
    print(num)