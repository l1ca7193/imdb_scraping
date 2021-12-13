#https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000233&ref_=filmo_ref_typ&mode=simple&page=1&sort=user_rating,desc&title_type=movie
#https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000233&ref_=filmo_ref_typ&mode=simple&page=1&sort=user_rating,desc&title_type=movie

import requests
import re
from bs4 import BeautifulSoup
import time
import csv

films = []

csv_file = open("Output/films226_directors.csv", "w", encoding="utf8", newline="\n")
csv_writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)

csv_writer.writerow(['DirectorName', 'DirectorCode', 'MovieName', 'MovieCode', 'Score', 'Year'])

with open("Input/imdb_codes.txt", "r") as _R:
    for line_id, line in enumerate(_R):
        begin_time = time.time()
        director_code = line.strip()
        URL = "https://www.imdb.com/name/" + director_code
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        director_name = soup.find("title").text
        director_name = re.sub(" - IMDb", "", director_name)

        page_index = 1
        while "Looking for movies":
            page = requests.get(
                url='https://www.imdb.com/filmosearch?',
                params={"explore": "title_type",
                    "role": director_code,
                    "ref_": "filmo_ref_typ",
                    "mode": "simple",
                    "page": page_index,
                    "sort": "user_rating,desc",
                    "title_type": "movie"}
            )

            soup = BeautifulSoup(page.content, "html.parser")
            movies = soup.find_all("div", {"class": "lister-item"})

            if len(movies) == 1 and "No results." in movies[0].text:
                break

            for movie in movies:
                try:
                    details = movie.find("div", {"class": "lister-item-image"}).a.img
                    title = details["alt"]
                    movie_code = details["data-tconst"]
                    score = movie.find("div", {"class": "col-imdb-rating"}).text.strip()
                    score = score.replace(",", ".")
                    year = movie.find("span", {"class": "lister-item-year"}).text
                    year = re.findall("\d{4}", year)

                    if score == "-":
                        score = "Unknown"
                    if year == []:
                        year = ["Unknown"]

                    csv_writer.writerow([director_name, director_code, title, movie_code, score, year[0]])
                    csv_file.flush()
                except Exception as error:
                    print(error)
                    pass
            time.sleep(2)
            page_index += 1
        print(f"{line_id + 1}) {director_name} ({director_code}) took {time.time() - begin_time:.1f} seconds")

