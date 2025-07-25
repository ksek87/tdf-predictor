# fetch data from procyclingstats api, fetch riders, tour de france data, stages, and results, save as json files
# we will fetch data from the last 5 years to start
import time
import os
import sys  
import procyclingstats as pcs
import pandas as pd
import ast
import json

# set the path to the data directory
TOUR_DATA_DIR = os.path.join(os.path.dirname(__file__), 'tour_data')
TOUR_DATA_CSV = 'tour_data.csv'
TOUR_STARTLIST_CSV = 'tour_startlist.csv'
TOUR_STAGES_CSV = 'tour_stages.csv'
STAGE_CLIMBS_CSV = 'stage_climbs.csv'
TOUR_RIDERS_CSV = 'tour_riders.csv'
YEARS = [2019, 2020]

def fetch_tdf_race(): # Note this method is failing due to issue in the procyclingstats library, it is not able to parse
    base_url = "race/tour-de-france/"
    races = []
    for year in YEARS:
        print(year)
        race = pcs.Race(base_url + str(year))
        races.append(race.parse())
    # convert races from json to dataframe    
    df = pd.DataFrame(races)
    return df    
    
def fetch_tdf_race_startlist():
    base_url = '/race/tour-de-france/'
    start = '/startlist'
    lists = []
    for year in YEARS: 
        startlist = pcs.RaceStartlist(base_url+str(year)+start)
        lists.append(startlist.parse())
    
    df = pd.DataFrame(lists)
    return df

def fetch_tdf_stages(tour_df):
    stages = []
    for _, row in tour_df.iterrows():
        year = row['year']
        try:
            # Check if 'stages' is already a list
            if isinstance(row['stages'], list):
                stage_list = row['stages']
            else:
                # Clean up the 'stages' string to ensure it is valid JSON
                stages_str = row['stages'].replace('""', '"').replace("'", '"')
                stage_list = json.loads(stages_str)  # Safely parse the stages column

            for stage in stage_list:
                stage_data = {
                    'year': year,
                    'stage_name': stage.get('stage_name', ''),
                    'stage_url': stage.get('stage_url', ''),
                    'date': stage.get('date', ''),
                }
                
                stage_data = pcs.Stage(stage_data['stage_url']).parse()
                stages.append(stage_data)
        except (json.JSONDecodeError, TypeError, AttributeError) as e:
            print(f"Error parsing stages for year {year}: {e}")
    
    df = pd.DataFrame(stages)
    return df

def fetch_tdf_climbs():
    return

def fetch_rider():
    return

def save_data(df, filename):
    if not os.path.exists(TOUR_DATA_DIR):
        os.makedirs(TOUR_DATA_DIR)
    file = os.path.join(TOUR_DATA_DIR, filename)
    df.to_csv(file, index=False)
    return

def main():
    race_df = fetch_tdf_race()
    save_data(race_df, TOUR_DATA_CSV)
    
    starts_df = fetch_tdf_race_startlist()
    save_data(starts_df, TOUR_STARTLIST_CSV)

    stages_df = fetch_tdf_stages(race_df)
    save_data(stages_df, TOUR_STAGES_CSV)

if __name__ == "__main__":
    main()
