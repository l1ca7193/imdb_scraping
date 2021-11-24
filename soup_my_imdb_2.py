#https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000233&ref_=filmo_ref_typ&mode=simple&page=1&sort=user_rating,desc&title_type=movie

#https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000233&ref_=filmo_ref_typ&mode=simple&page=1&sort=user_rating,desc&title_type=movie


import requests
import re
from bs4 import BeautifulSoup
ii = 1
films = []

while ii < 3:
    nm = "nm0000233"
    
    startURL = "https://www.imdb.com/filmosearch/?explore=title_type&role="
    midURL = "&ref_=filmo_ref_typ&mode=simple&page="
    endURL = "&sort=user_rating,desc&title_type=movie"
    
    URL = startURL + nm + midURL + str(ii) + endURL 
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    page_coltitle = soup.find_all("div", class_="col-title")
    page_colimdbrating = soup.find_all("div", class_="col-imdb-rating")

    for md, ti in zip(page_colimdbrating, page_coltitle):
        try:
            score_strong = md.find("strong").get_text()
            score = score_strong.replace(" ","")
            filmname = ti.find("a").get_text()
            title_code = re.findall("tt\d{1,7}", str(ti))

            if score_strong != "IMDbRating":
                films.append([filmname, title_code[0], score.strip()])                
            else:
                pass
        except Exception as error:
            pass
    ii+=1

for e in films:
    print(e)

#end

