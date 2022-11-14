import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def constructor_points(year, team):
    '''
    INPUTS
    year: (String) year that we want to examine
    team: (String) team code of team we want to examine
          Note that the team code should be in all lowercase

    OUTPUTS
    df: data frame of how a team's points increase after each round of a season
    '''
    round_url = "http://ergast.com/api/f1/" + year
    rounds = requests.get(round_url)

    soup = BeautifulSoup(rounds.content,'html.parser')


    count = int(soup.mrdata['total'])

    points = 0


    points_dict = {}
    delta_lst = []
    round_lst = [i + 1 for i in range(count)]
    dates_lst = []


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

        date_url = "http://ergast.com/api/f1/" + year + '/' + round
        page2 = requests.get(date_url)
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        date = soup2.find('date').text
        dates_lst.append(date)


    points_dict['point deltas'] = delta_lst
    points_dict['date'] = dates_lst

    df = pd.DataFrame(points_dict, index = round_lst)

    return df

print(constructor_points('2010', 'force_india'))
