# importare:
# nome ok
# lista dei film DIV filmo-category-section + imdb score
# abbinare il trailer al film

import requests
import re
from bs4 import BeautifulSoup
URL = "https://www.imdb.com/name/nm0000186/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("title").get_text()
#title_clean = re.findall(" - IMDb",title)
title_clean = re.sub(" - IMDb", "", title)
print (title_clean)

#films_div = soup.find_all("div", {"class":"filmo-category-section"})
films_div = soup.find_all("div", class_="filmo-category-section")

for e in films_div:
    print(e.find("a")
