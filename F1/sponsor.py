import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def sponsors(constructor):
    '''
    INPUTS
    constructor: (String) team code of the constructor we want to examine

    OUTPUTS
    df: dataframe of the sponsors of the livery sponsors of that team seperated
    by year
    '''

    url2 = 'https://en.wikipedia.org/wiki/Formula_One_sponsorship_liveries'
    sponsor_page = requests.get(url2)

    soup2 = BeautifulSoup(sponsor_page.content, 'html.parser')

    team = soup2.find(id = constructor)

    header = team.parent

    table = header.find_next_sibling('table')

    df = pd.read_html(str(table))
    df = pd.concat(df)

    df['Year'] = df['Year'].replace({"\[(.*?)\]":""}, regex=True).astype('string')
    df["Livery sponsor(s)"] = df["Livery sponsor(s)"].astype('string')
    df["Additional major sponsor(s)"] = df["Additional major sponsor(s)"].astype('string')
    df.set_index('Year', inplace = True)
    df.drop("Main colour(s)", axis = 1, inplace = True)
    df.drop('Additional colour(s)', axis = 1, inplace = True)

    return df
