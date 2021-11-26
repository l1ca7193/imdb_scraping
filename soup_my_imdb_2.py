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
with open("imdb_codes.txt","r") as f:
    lines = f.readlines()
    for id, line in enumerate(lines):
        begin_time = datetime.datetime.now()
        codiceRegista = line.strip()
        URL = "https://www.imdb.com/name/" + codiceRegista
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        regista = soup.find("title").get_text()
        regista_clean = re.sub(" - IMDb", "", regista)

        ii = 1
        while ii < 3:
            startURL = "https://www.imdb.com/filmosearch/?explore=title_type&role="
            midURL = "&ref_=filmo_ref_typ&mode=simple&page="
            endURL = "&sort=user_rating,desc&title_type=movie"
            
            URL = startURL + codiceRegista + midURL + str(ii) + endURL 
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
                        films.append([regista, codiceRegista, filmname, title_code[0], score.strip(), year[0]])           
                    else:
                        pass
                except Exception as error:
                    pass
            time.sleep(6)
            ii+=1
        print(str(id+1)+ " " + codiceRegista + " " + str(datetime.datetime.now() - begin_time))

pandas.DataFrame(films).to_csv('films226_directors.csv', index_label = "Index", header  = ['director name','director code','film name','title code','score', 'year'])    