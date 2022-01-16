# male first names

import bs4
import requests

URL = "https://www.babycenter.in/a25010813/bengali-baby-names"
page = requests.get(URL)

print(page.text)

