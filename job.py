import requests
import bs4 as bs
from urllib.parse import urlencode
import json
import os

import pandas as pandas
import numpy as np
from datetime import datetime

job_url = []

# Building the query for GET request
def build_job_query(keyword, location):
    job_search = {
        "q" : keyword,
        "l" : location
    }
    job_query = "https://hk.indeed.com/jobs?" + urlencode(job_search)

# Getting list of job links
def get_job_links(job_query):
    data = requests.get(job_query)
    resp = data.text.encode('utf-8')
    soup = bs.BeautifulSoup(resp,'lxml')
    job_listings = soup.find_all("a",class_="turnstileLink")

    for job in job_listings:
        job_url.append("https://hk.indeed.com/"+job["href"])

# Testing crawling data from the first job link
get_job_links(build_job_query("Digital Marketing","Hong Kong"))

print(job_url[0])


