import pandas as pd
import os
import sys

TOUR_DATA_DIR = os.path.join(os.path.dirname(__file__), 'tour_data')
CLEAN_DATA_DIR = os.path.join(os.path.dirname(__file__), 'clean_data')
TOUR_DATA_CSV = 'tour_data.csv'
TOUR_STARTLIST_CSV = 'tour_startlist.csv'
TOUR_STAGES_CSV = 'tour_stages.csv'
STAGE_CLIMBS_CSV = 'stage_climbs.csv'
TOUR_RIDERS_CSV = 'tour_riders.csv'

def load_data(filename):
    file_path = os.path.join(TOUR_DATA_DIR, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file {filename} not found in {TOUR_DATA_DIR}")
    df = pd.read_csv(file_path)
    return df

def race_data_cleaning(df):
    
    return df

def startlist_data_cleaning(df):
    # Convert the 'startlist' column (JSON strings) into a list of dictionaries
    df['startlist'] = df['startlist'].apply(eval)  # Convert JSON strings to Python objects
    # Explode the list of dictionaries into individual rows
    df = df.explode('startlist', ignore_index=True)
    # Normalize the dictionaries into separate columns
    df = pd.json_normalize(df['startlist'])
    return df

def process_startlist():
    startlist_df = load_data(TOUR_STARTLIST_CSV)
    # clean the startlist data
    cleaned_startlist_df = startlist_data_cleaning(startlist_df)
    # save the cleaned startlist data
    cleaned_startlist_file = os.path.join(CLEAN_DATA_DIR, 'cleaned_' + TOUR_STARTLIST_CSV)
    cleaned_startlist_df.to_csv(cleaned_startlist_file, index=False)
    return

def main():
    
    if not os.path.exists(CLEAN_DATA_DIR):
        os.makedirs(CLEAN_DATA_DIR) 
    
    process_startlist
    print("Startlist data cleaned and saved.")
    

if __name__ == "__main__":
    main()
