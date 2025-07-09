# fetch data from procyclingstats api, fetch riders, tour de france data, stages, and results, save as json files
# we will fetch data from the last 5 years to start
import time
import procyclingstats as pcs
import pandas as pd

def fetch_tdf_race(): # Note this method is failing due to issue in the procyclingstats library, it is not able to parse
    base_url = "race/tour-de-france/"
    years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    
    races = []
    
    for year in years:
        print(year)
        race = pcs.Race(base_url + str(year))
        race.parse()
        races.append(race)
    
    # convert races from json to dataframe    
    df = pd.DataFrame(races)
    print(df.head())
    return df    
    
def fetch_tdf_race_startlist():
    return 
def fetch_tdf_stages():
    return

def fetch_tdf_climbs():
    return

def fetch_rider():
    return


def main():
    race_df = fetch_tdf_race()
    print("fetched tour races")
    return

if __name__ == "__main__":
    main()
    