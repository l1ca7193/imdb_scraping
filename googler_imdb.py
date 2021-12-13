import subprocess
import re
from random import randint
import time

with open("Input/Directors.list", "r") as _R:
    with open("Output/imdb_urls.txt", "w") as _W:
        for line in _R:
            director = line.strip()
            query = subprocess.run(["googler", "-n", "1", "imdb.com", director, "--json"], capture_output=True, text=True)
            query = query.stdout
            code = re.findall("nm\d{1,7}",query)
            print(f"{director}: {code[0]}")
            _W.write(f"{director},https://www.imdb.com/name/{code[0]}\n")

            # TIME SLEEP IS A MUST OR GOOGLE WILL SEND YOU TO HORNY JAIL
            wait = randint(100,200)
            print(f"I'm sleeping for {wait} seconds")
            time.sleep(wait)
