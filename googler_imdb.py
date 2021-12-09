import subprocess
import re
from random import randint
import time

with open("registi.list","r") as f:
        lines = f.readlines()
        for line in lines:
                regista = line.strip()
                query = subprocess.run(["googler", "-n", "1", "imdb.com", regista, "--json"], capture_output=True, text=True)
                query = query.stdout
                code = re.findall("nm\d{1,7}",query)
                try:
                        print(regista + " " + code[0])
                        with open("imdb_urls.txt", "a+") as ff:
                                ff.write(regista+","+"https://www.imdb.com/name/"+code[0]+"\n")
                except:
                        print("The query is empty")
                # TIME SLEEP IS A MUST OR GOOGLE WILL SEND YOU TO HORNY JAIL
                stop = randint(100,200)
                print("I'm sleeping for "+str(stop)+"s")
                time.sleep(stop)
