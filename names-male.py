# male first names

from bs4 import BeautifulSoup
from selenium import webdriver
import requests

driver = webdriver.Chrome()
URL = "https://danishmom.com/danish-boy-names/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

print(results.prettify())

