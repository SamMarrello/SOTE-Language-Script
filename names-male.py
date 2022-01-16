# male first names

import bs4
import requests

URL = "https://danishmom.com/danish-boy-names/"
page = requests.get(URL)

print(page.text)

