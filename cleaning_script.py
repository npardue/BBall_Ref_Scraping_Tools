def clean_season(season = None, url = None, year = None):
    """Cleans dataframes scraped from basketball-reference.com, and overwrites them.

    Keyword arguments:
    season = str; 'leagues' for regular season stats, or 'playoffs' for playoff stats
        - Same naming as in the get_player_stats function in soup_bballref.py

    url = str, the folder within our '/data/raw/' folder where the dataframes are stored. Same
        naming as in the get_player_stats function in soup_bballref.py
            - seasonal totals = 'totals'
            - per game averages = 'per_game'
            - per 36 minutes = 'per_minute'
            - per 100 possessions = 'per_poss'
            - advanced stats = 'advanced'
            - shooting stats = 'shooting'
            - adjusted shooting stats = 'adj_shooting'
    year = int, the season of the .csv file to be cleaned


    eg) clean_season(season = 'leagues', url = 'totals', year = 2019)
            will clean total stats for the 2018-2019 regular season.
    """
    # Importing packages
    import pandas as pd
    import os

    # Creating a path for our file to save to if it doesn't already exist
    if not os.path.exists(f'data/clean/{season}/{url}/'):
        os.makedirs(f'data/clean/{season}/{url}/')
        print(f'Folder Created: data/clean/{season}/{url}/')


    #Loading in dataframe
    #df = pd.read_csv(f'/Users/npardue/Desktop/Capstone/data/raw/{folder}/{year}_stats.csv')
    df = pd.read_csv(f'data/raw/{season}/{url}/{year}_stats.csv')

    # Adding a 'current year' column for organizational purposes.
    df['current_year'] = year


    # Some players were traded during the middle of a season, and as such will have 3+ rows.
    # The first will be a player's total stats for the season (df.Tm == TOT), and the following
    # will be stats for each of the teams the player recorded stats for, and subsequently drop them
    # from the dataframe. 
    df= df.drop(df.loc[df.Player.duplicated() == True].index, axis=0)

    # Dropping a leftover row that served as a header on the original document.
    df = df.drop(df.loc[df['Player'].isna()].index, axis=0)


    # Removing the '*' denoting any player that has made the Hall of Fame, as
    # not all .csv files to be used are formatted the same way.
    df.Player = df.Player.apply(lambda x: x.replace('*', ''))


    # Removing the unnecesary 'Unnamed: 0' column.
    df = df.drop(columns='Unnamed: 0')

    # Re-saving 
    df.to_csv(f'data/clean/{season}/{url}/{year}_stats.csv')

    # So we have a way of tracking where we're at in the cleaning process
    print(f'{season} stats for {url} {year} cleaned! {2019 - year} seasons to go.')