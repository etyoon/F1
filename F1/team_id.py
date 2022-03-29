import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

url = 'http://ergast.com/api/f1/2010/constructors'
page = requests.get(url)

data = []

list_header = []
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
    constructors.append(id['constructorid'])
dict["team_code"] = constructors
print(dict)

dataFrame = pd.DataFrame(dict, index  = range(12))

root = 'F1'
dataFrame.to_csv(root + '/' + 'TeamCodes.csv')
