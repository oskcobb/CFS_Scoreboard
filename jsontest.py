import json
import requests

name = "Vollyball"

r = requests.get('https://raw.githubusercontent.com/oskcobb/CFS_Scoreboard-Themes/main/themes.json')
themes = json.loads(r.text)
for theme in themes["themes"]:
    print(theme)
    print(name)
    print()
    if theme["name"] == name:
        temp = theme["name"]
        url = theme["url"]
        print(url)
        try:
            print(url)
            dl = requests.get(url).content
        except:
            print("Error")
            pass
        print(dl)