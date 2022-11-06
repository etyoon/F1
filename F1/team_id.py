import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

#creating teamcodes for teams within a year and turning them into csv files
year = '2010'

url = 'http://ergast.com/api/f1/' + year + '/constructors'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

dict = {}
constructors = []
TeamName = []
ids = soup.find_all("constructor")
names = soup.find_all('name')



for name in names:
    TeamName.append(name.text)
dict['name'] = TeamName


for id in ids:
    if id['constructorid'].title() == "Red_Bull":
        constructors.append("Red_Bull_Racing")
    else:
        constructors.append(id['constructorid'].title())
dict["team_code"] = constructors


dataFrame = pd.DataFrame(dict, index  = range(12))

print(dataFrame.head)
