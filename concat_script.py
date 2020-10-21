def concat_frames():
    """ This is a function that will concatenate all .csv files within a folder into one .csv file.
    """
    import glob
    import os
    import pandas as pd

    # Creating a path for our file to save to if it doesn't already exist
    if not os.path.exists(f'data/clean/concat/'):
        os.makedirs(f'data/clean/concat/')
        print(f'Folder Created: data/clean/concat/')

    # File path of the folder containing .csv files of interest
    path = r'/data/combined'

    # Joining the file paths and names into a list of files
    all_files = glob.glob(os.path.join(path, "*.csv"))

    # Creating a dataframe for each file in all_files
    df_from_each_file = (pd.read_csv(f) for f in all_files)

    # Columns to drop from final dataframe
    columns = 'Unnamed: 0|Unnamed: 0.1|Unnamed: 0_play_totals|Pos_play_totals|Age_play_totals|\
    Tm_play_totals|Unnamed: 0_reg_36|Pos_reg_36|Age_reg_36|Tm_reg_36|\
    G_reg_36|GS_reg_36|MP_reg_36|current_year_reg_36|Unnamed: 0_play_36|Pos_play_36|Age_play_36|\
    Tm_play_36|G_play_36|GS_play_36|MP_play_36|current_year_play_36|Unnamed: 0_reg_adv|Pos_reg_adv|\
    Age_reg_adv|Tm_reg_adv|G_reg_adv|MP_reg_adv|current_year_reg_adv|Unnamed: 0_play_adv|\
    Pos_play_adv|Age_play_adv|Tm_play_adv|G_play_adv|MP_play_adv|\
    current_year_play_adv|Unnamed: 0_reg_adv|Pos_reg_adv|Age_reg_adv|Tm_reg_adv|G_reg_adv|MP_reg_adv|\
    current_year_reg_adv|Unnamed: 0_play_adv|Pos_play_adv|Age_play_adv|Tm_play_adv|G_play_adv|\
    MP_play_adv|current_year_play_adv'

    columns = columns.split('|')

    concatenated_df = concatenated_df.drop(columns=columns)

    # Creating an indicator of whether or not a player made the playoffs for any given year
    concatenated_df['made_playoffs'] = np.where(concatenated_df.current_year_play_totals != 0, 1, 0)
    # Sorting the frame by year.
    concatenated_df = concatenated_df.sort_values(by='current_year', ascending=True)

    # Creating a path for our file to save to if it doesn't already exist
    if not os.path.exists('data/clean/all_years/'):
        os.makedirs('data/clean/all_years')
        print('Folder Created: data/clean/all_years/')

    concatenated_df.to_csv('data/clean/all_years')

    return