import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

#creating teamcodes for teams within a year and turning them into csv files

url = 'http://ergast.com/api/f1/2010/constructors'
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
    constructors.append(id['constructorid'].title())
dict["team_code"] = constructors


dataFrame = pd.DataFrame(dict, index  = range(12))

root = 'F1'
dataFrame.to_csv(root + '/' + 'TeamCodes.csv')

#creating a csv of teams and sponsors, need work
sponsors = {}
for team in dict['name']:
    sponsors[team] = []

url2 = 'https://en.wikipedia.org/wiki/Formula_One_sponsorship_liveries'
sponsor_page = requests.get(url2)

soup2 = BeautifulSoup(sponsor_page.content, 'html.parser')

for team in dict['team_code']:
    teams = soup2.find_all(id = team)
    for tags in teams:
        if

#new_dataframe = dataFrame.filter(['name'])
