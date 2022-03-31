import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

url2 = 'https://en.wikipedia.org/wiki/Formula_One_sponsorship_liveries'
sponsor_page = requests.get(url2)

soup2 = BeautifulSoup(sponsor_page.content, 'html.parser')


for siblings in soup2.find(id = 'Red_Bull_Racing').next_siblings:
    if siblings
