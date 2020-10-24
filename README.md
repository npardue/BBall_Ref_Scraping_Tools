# BBall_Ref_Scraping_Tools
Python scripts for scraping NBA player information from basketball-reference.com.

Uploading some scripts that I used to scrape, clean, and combine tables from basketball-reference.com for my [capstone project], where I estimated how many additional seasons an NBA player could be expected to play.


## Order of Use and their Doc Strings
### 1. soup_bballref.py
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
            will pull total stats for the 2018-2019 playoff season.

### 2. cleaning_script.py
Loads in raw dataframes saved by get_player_stats(), cleans them, and saves them to a new datafile in a 'data/clean/{folder}/{year}_stats.csv' format.
File paths are currently hard-coded for my local machine, so please update lines 19 & 44 accordingly.


    Keyword arguments:

    folder = string, the folder within our 'data' folder where the dataframes are stored
    year = int, the season of the .csv file to be cleaned

    Ex.
    clean_bballref('regseason', 2000)
            - Would access the 1999-2000 regular season's .csv file, clean it, and then
            save a new copy of that file on top of the existing file.

### 3. merging_script.py
This function will merge a year's regular season and playoff stats into one .csv file, and save them to a new datafile in a 'data/clean/combined/{year}_stats.csv' format.


### 4. concat_script.py
This function will join all of the cleaned, merged, .csv files for each specified year, and save them to a new folder in a 'data/clean/all_years/' format.
Again, a smidge of hard-coding was done-- this time to remove columns that were deemed redundant (see line 23).



https://github.com/npardue/estimating_addtl_NBA_seasons
