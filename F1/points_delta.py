import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

year = "2010"
round_url = "http://ergast.com/api/f1/" + year
rounds = requests.get(round_url)

soup = BeautifulSoup(rounds.content,'html.parser')


count = int(soup.mrdata['total'])

points = 0

team = "force_india"

#for i in range(count):
#    round = str(i + 1)
points_url = "http://ergast.com/api/f1/" + year + "/19" + "/constructorStandings"
points = requests.get(points_url)
soup = BeautifulSoup(points.content, 'html.parser')

thing = soup.find(constructorid = team)
new_points = thing.parent['points']
print(new_points)
