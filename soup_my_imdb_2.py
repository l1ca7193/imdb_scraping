#https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000233&ref_=filmo_ref_typ&mode=simple&page=1&sort=user_rating,desc&title_type=movie

#https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000233&ref_=filmo_ref_typ&mode=simple&page=1&sort=user_rating,desc&title_type=movie


import requests
import re
from bs4 import BeautifulSoup
ii = 1
film_score = []
film_name = []
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

    for e in page_coltitle:
        try:
            filmname = e.find("a").get_text()
            title_code = re.findall("tt\d{1,7}", str(e))
            film_name.append([filmname, title_code[0]])
        except Exception as error:
            pass
            
    for e in page_colimdbrating:
        try:
            score_strong = e.find("strong").get_text()
            score = score_strong.replace(" ","")
            film_score.append(score.strip())            
        except Exception as error:
            pass
    ii+=1
print(film_name)
clean_fscore = [ x for x in film_score if x != "IMDbRating" ]
print(clean_fscore)
#end

