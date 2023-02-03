import time
from bs4 import BeautifulSoup
import requests

url = ""

def flix(url):
    client = requests.session()
    r = client.get(url)
    soup = BeautifulSoup (r.text, "html.parser")
        links = soup.select('a[href*="gdtot"]')
        if len(links) == 0:
             links = soup.select('a[href*="filepress"]')
        gd_txt = f"Total Links Found : {len(links)}\n\n"
        print(gd_txt)
        for a in links:
             link = a["href"]
             print(link) 

print(flix(url))
