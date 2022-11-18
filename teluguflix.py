import time
from bs4 import BeautifulSoup
import requests

url = "https://teluguflix.xyz/sita-ramam-2022-hindi-full-movie-download-dsnp-web-dl-1080p-720p-576p-avc-aac-2-0-esub/"

def flix(url):
    client = requests.session()
    r = client.get(url).text
    y = r.split('id="download"')[-1]
    f = y.split("</ul>") [0]
    soup = BeautifulSoup (f, "html.parser")
    for a in soup.find_all("a"):
              c = a.get("href")
              print(c)

print(flix(url))
