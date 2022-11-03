import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

url2 = 'https://en.wikipedia.org/wiki/Formula_One_sponsorship_liveries'
sponsor_page = requests.get(url2)

soup2 = BeautifulSoup(sponsor_page.content, 'html.parser')

team = soup2.find(id = 'Alfa_Romeo')

header = team.parent

table = header.find_next_sibling('table')

df = pd.read_html(str(table))
df = pd.concat(df)
df.to_csv(r'C:\Users\17735\Desktop\F1 Python\F1\sponsor.csv', index = False)
