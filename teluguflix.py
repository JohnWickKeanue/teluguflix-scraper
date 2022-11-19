import time
from bs4 import BeautifulSoup
import requests

url = "https://teluguflix.xyz/aha-naa-pellanta-2022-season01-all-episodes-download-zee5-web-dl-4k-2160p-1080p-720p-480p-hevc-avc-dd5-1-192kbps-esubs/"

def flix(url):
    client = requests.session()
    Jack = client.get(url).text
    soup = BeautifulSoup (Jack, "html.parser")
    for a in soup.find_all("a"):
              c = a.get("href") 
              if "gdtot" in c:
                     t = client.get(c).text
                     soupt = BeautifulSoup(t, "html.parser")
                     title = soupt.title
                     gd_txt = f"{(title.text).replace('GDToT | ' , '')}\n{c}\n\n"
                     print(gd_txt) 

print(flix(url))
