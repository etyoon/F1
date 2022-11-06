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
points_dict = {}
delta_lst = []
round_lst = [i + 1 for i in range(count)]


for i in range(count):
    round = str(i + 1)
    points_url = "http://ergast.com/api/f1/" + year +'/' +round + "/constructorStandings"
    page = requests.get(points_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    thing = soup.find(constructorid = team)
    new_points = float(thing.parent['points'])
    delta = new_points - float(points)
    points = new_points
    delta_lst.append(delta)

points_dict['point deltas'] = delta_lst

df = pd.DataFrame(points_dict, index = round_lst)

print(df.head)
