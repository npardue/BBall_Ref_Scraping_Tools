def get_player_stats(season = None, url = None, year = None):
    '''
    Function to scrape player stats from bballref, and return them as a .csv file in a 'data' folder.

    season = str; 'leagues' for regular season stats, or 'playoffs' for playoff stats
        - Will also double as the parent folder name for folders housing .csv files

    url = str; the type of stats to pull. Is appended on to the end of our source website
        - Will also double as the name of the folder we're saving our .csv files into
            - seasonal totals = 'totals'
            - per game averages = 'per_game'
            - per 36 minutes = 'per_minute'
            - per 100 possessions = 'per_poss'
            - advanced stats = 'advanced'
            - shooting stats = 'shooting'
            - adjusted shooting stats = 'adj_shooting'

    year = int; year we would like stats for.
        - Will also double as a part of the naming convention for our .csv files


    eg) get_player_stats(season = 'leagues', url = 'totals', year = 2019)
            will pull total stats for the 2018-2019 regular season.
    '''
    # importing necessary packages
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import os

    # Creating a path for our file to save to if it doesn't already exist
    if not os.path.exists(f'data/raw/{season}/{url}/'):
        os.makedirs(f'data/raw/{season}/{url}/')
        print(f'Folder Created: data/raw/{season}/{url}/')


    # NBA season we will be analyzing
    year = int(year)

    # this is the HTML from the given URL
    source = requests.get(f'https://www.basketball-reference.com/{season}/NBA_{year}_{url}.html').text

    # instantiating the Soup
    soup = BeautifulSoup(source, features='lxml')

    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
    headers = headers[1:]

    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

    df = pd.DataFrame(player_stats, columns = headers)

    df.to_csv(f'data/raw/{season}/{url}/{year}_stats.csv')

    # So we have a way of tracking where we're at in the downloads
    print(f'{url} stats for the {year} {season} collected! {2019 - year} seasons to go.')
