#https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000233&ref_=filmo_ref_typ&mode=simple&page=1&sort=user_rating,desc&title_type=movie
#https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000233&ref_=filmo_ref_typ&mode=simple&page=1&sort=user_rating,desc&title_type=movie

import requests
import re
from bs4 import BeautifulSoup
import time
import datetime
import numpy
import pandas

films = []

begin_time = datetime.datetime.now()
print(datetime.datetime.now())
with open("imdb_codes_short.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        begin_time = datetime.datetime.now()
        regista = line.strip()
        ii = 1
        while ii < 3:
            startURL = "https://www.imdb.com/filmosearch/?explore=title_type&role="
            midURL = "&ref_=filmo_ref_typ&mode=simple&page="
            endURL = "&sort=user_rating,desc&title_type=movie"
            
            URL = startURL + regista + midURL + str(ii) + endURL 
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, "html.parser")

            page_coltitle = soup.find_all("div", class_="col-title")
            page_colimdbrating = soup.find_all("div", class_="col-imdb-rating")

            for md, ti, ye in zip(page_colimdbrating, page_coltitle, page_coltitle):
                try:
                    score_strong = md.find("strong").get_text()
                    score = score_strong.replace(" ","")

                    year_span= ye.find("span", class_="lister-item-year text-muted unbold").get_text()
                    year = re.findall("\d{4}", str(year_span))

                    filmname = ti.find("a").get_text()
                    title_code = re.findall("tt\d{1,7}", str(ti))
                    if score_strong != "IMDbRating":
                        films.append([filmname, title_code[0], score.strip(), year[0]])           
                    else:
                        pass
                except Exception as error:
                    pass
            time.sleep(5)
            ii+=1
        print(regista + " " + str(datetime.datetime.now() - begin_time))

pandas.DataFrame(films).to_csv('films.csv', index_label = "Index", header  = ['film name','title code','score', 'year'])    