# importazione film per regista:
# nome ok (già presente)
# lista dei film DIV filmo-category-section + imdb score
## https://www.imdb.com/title/tt0397764
# abbinare il trailer al film
# https://www.imdb.com/title/tt0166444/ratings/?ref_=tt_ov_rt

import requests
import re
from bs4 import BeautifulSoup
URL = "https://www.imdb.com/name/nm0002031/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# solo il titolo
title = soup.find("title").get_text()
#
title_clean = re.sub(" - IMDb", "", title)
print (title_clean)

# title codes
#title_code = re.findall("tt\d{1,7}", str(title))

#films_div = soup.find_all("div", {"class":"filmo-category-section"})
films = []
ttcodes = []
films_row_even = soup.find_all("div", class_="filmo-row even")
for e in films_row_even:
    # <a> link title codes
    link = e.find("a").get_text()
    # title codes
    title_code = re.findall("tt\d{1,7}", str(e))
    films.append(link + "," + title_code[0])
    ttcodes.append(title_code[0])

films_row_odd = soup.find_all("div", class_="filmo-row odd")
for e in films_row_odd:
    # <a> link title codes
    link = e.find("a").get_text()
    # title codes
    title_code = re.findall("tt\d{1,7}", str(e))
    films.append(link + "," + title_code[0])
    ttcodes.append(title_code[0])
    
films_no_dup = list(dict.fromkeys(films))
#films_no_dup_100 = del films_no_dup[100:]

for i in ttcodes:
    print(i)

#<span class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV">6.6</span>
#<span class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV">5.0</span>


