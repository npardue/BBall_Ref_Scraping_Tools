def merge_reg_playoffs(year):
    """***This hard-coded***, and should only be ran after running get_player_stats(), and clean_season().
    A function to merge a year's regular season and playoff stats into one .csv file.

    Params:
    year- The year of stats to merge.

    eg) for i in range(1979, 2020):
            merge_reg_playoffs(i)
        will merge regular season and playoffs total stats, per_minute stats, and advanced stats
    """
    # Importing packages
    import pandas as pd
    import os
    from functools import reduce

    # Creating a path for our file to save to if it doesn't already exist
    if not os.path.exists(f'data/clean/combined/'):
        os.makedirs(f'data/clean/combined/')
        print(f'Folder Created: data/clean/combined/')

    # Setting a list of folder names to iterate through.
    seasons = ['leagues', 'playoffs']
    folders = ['totals', 'per_minute', 'advanced']

    names = ['reg_totals', 'play_totals', 'reg_36', 'play_36', 'reg_adv', 'play_adv']

    # Loading in the dataframes to merge and setting them to a list.
    reg_totals = pd.read_csv(f'data/clean/{seasons[0]}/{folders[0]}/{year}_stats.csv')
    reg_36 = pd.read_csv(f'data/clean/{seasons[0]}/{folders[1]}/{year}_stats.csv')
    reg_adv = pd.read_csv(f'data/clean/{seasons[0]}/{folders[2]}/{year}_stats.csv')
    play_totals = pd.read_csv(f'data/clean/{seasons[1]}/{folders[0]}/{year}_stats.csv')
    play_36 = pd.read_csv(f'data/clean/{seasons[1]}/{folders[1]}/{year}_stats.csv')
    play_adv = pd.read_csv(f'data/clean/{seasons[1]}/{folders[2]}/{year}_stats.csv')

    data_frames = [reg_totals, play_totals, reg_36, play_36, reg_adv, play_adv]

    # Naming each dataframe to allow proper suffixing where needed upon merger.
    for i in range(0, len(names)):
        data_frames[i].name = names[i]

    # Merging Regular Season and Playoff frames.
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=['Player'],
                                                    how='left',
                                                    suffixes=(None, f'_' + right.name)),
                       data_frames).fillna(0)

    # Saving the merged frame as a .csv file into the 'combined' folder.
    pd.DataFrame.to_csv(df_merged, f'data/clean/combined/{year}_stats.csv')

    # So we have a way of tracking where we're at in the cleaning process
    print(f'Stats for the {year} season merged! {2019 - year} seasons to go.')

