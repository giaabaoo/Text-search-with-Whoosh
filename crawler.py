crawl_list = []

import requests
from bs4 import BeautifulSoup as soup
from pathlib import Path
from datetime import datetime, timedelta
from urllib.request import urlopen as uReq
from dateutil import parser
import pytz
import validators
import pdb

import os

Path("./news_data").mkdir(parents=True, exist_ok=True)

count = 0
url = "https://e.vnexpress.net/"

# Opening up the website, grabbing the page
uFeedOne = uReq(url, timeout=5)
page_one = uFeedOne.read()
uFeedOne.close()

# html parser
soup_one = soup(page_one, "html.parser")

crawl_limit = 30

for a in set(soup_one.find_all('a', href=True)):
    link = a.attrs['href']

    if validators.url(link):
        response = requests.get(link)
        doc_name = "doc" + str(count) + ".txt"
        subsoup = soup(response.text, 'html.parser')
        if response.text != " ":
            with open(os.path.join("./news_data/", doc_name), "w") as f:
                for data in subsoup.find_all("p"):
                    ss = data.get_text()
                    f.write(ss)

            count += 1

    if count == crawl_limit:
        break
    


