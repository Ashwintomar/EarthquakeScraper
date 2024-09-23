import pandas as pd
import os
import scrape_riseq
import scrape_earthquaketrack
import scrape_isr
import scrape_earthquakelist

def run_scrapers_and_combine():
    # Run the scrapers
    scrape_riseq.scrape_riseq()
    scrape_earthquaketrack.scrape_earthquaketrack()
    scrape_isr.scrape_isr()
    scrape_earthquakelist.scrape_earthquakelist()

    # Load the CSV files into DataFrames
    df_riseq = pd.read_csv('riseq_earthquake_data.csv')
    df_earthquaketrack = pd.read_csv('earthquaketrack_earthquake_data.csv')
    df_isr = pd.read_csv('isr_earthquake_data.csv')
    df_earthquakelist = pd.read_csv('earthquakelist_earthquake_data.csv')

    # Add source information to each DataFrame
    df_riseq['Source'] = 'RISEQ'
    df_earthquaketrack['Source'] = 'Earthquaketrack'
    df_isr['Source'] = 'ISR'
    df_earthquakelist['Source'] = 'Earthquakelist'

    # Process RISEQ data
    if 'Event Name' in df_riseq.columns:
        df_riseq = df_riseq.rename(columns={'Event Name': 'Location', 'Origin Time': 'Date and Time', 'Event ID': 'ID'})
    if 'Latitude, Longitude' in df_riseq.columns:
        df_riseq = df_riseq.rename(columns={'Latitude, Longitude': 'Coordinates'})
    if 'Magnitude, Depth' in df_riseq.columns:
        df_riseq['Magnitude and Depth'] = df_riseq['Magnitude, Depth'].apply(lambda x: f"Magnitude: {x.split(',')[0].strip()}, Depth: {x.split(',')[1].strip()}")
        df_riseq = df_riseq.drop(columns=['Magnitude, Depth'])

    # Process Earthquaketrack data
    if 'Time' in df_earthquaketrack.columns:
        df_earthquaketrack = df_earthquaketrack.rename(columns={'Time': 'Date and Time'})
    if 'Magnitude' in df_earthquaketrack.columns and 'Depth' in df_earthquaketrack.columns:
        df_earthquaketrack['Magnitude and Depth'] = df_earthquaketrack.apply(lambda row: f"Magnitude: {row['Magnitude']}, Depth: {row['Depth']}", axis=1)
        df_earthquaketrack = df_earthquaketrack.drop(columns=['Magnitude', 'Depth'])

    # Process ISR data
    if 'Date' in df_isr.columns:
        df_isr = df_isr.rename(columns={'Date': 'Date and Time'})
    if 'No.' in df_isr.columns:
        df_isr = df_isr.rename(columns={'No.': 'ID'})
    lat_col = next((col for col in df_isr.columns if 'lat' in col.lower()), None)
    long_col = next((col for col in df_isr.columns if 'long' in col.lower()), None)
    if lat_col and long_col:
        df_isr['Coordinates'] = df_isr[lat_col].astype(str) + ', ' + df_isr[long_col].astype(str)
        df_isr = df_isr.drop(columns=[lat_col, long_col])
    mag_col = next((col for col in df_isr.columns if 'magnitude' in col.lower()), None)
    depth_col = next((col for col in df_isr.columns if 'depth' in col.lower()), None)
    if mag_col and depth_col:
        df_isr['Magnitude and Depth'] = df_isr.apply(lambda row: f"Magnitude: {row[mag_col]}, Depth: {row[depth_col]}", axis=1)
        df_isr = df_isr.drop(columns=[mag_col, depth_col])

    # Process Earthquakelist data
    if 'Date and Time' in df_earthquakelist.columns:
        df_earthquakelist = df_earthquakelist.rename(columns={'Date and Time': 'Date and Time'})
    if 'Magnitude' in df_earthquakelist.columns:
        df_earthquakelist['Magnitude and Depth'] = df_earthquakelist['Magnitude'].apply(lambda x: f"Magnitude: {x}")
        df_earthquakelist = df_earthquakelist.drop(columns=['Magnitude'])

    # Combine the DataFrames
    combined_df = pd.concat([df_riseq, df_earthquaketrack, df_isr, df_earthquakelist], ignore_index=True)

    # Standardize column names
    column_mapping = {
        'Location': 'Location',
        'Date and Time': 'Date and Time',
        'Coordinates': 'Coordinates',
        'Magnitude and Depth': 'Magnitude and Depth',
        'Event Type': 'Event Type',
        'ID': 'ID',
        'Source': 'Source'
    }
    combined_df = combined_df.rename(columns=column_mapping)

    # Ensure all necessary columns exist
    for col in column_mapping.values():
        if col not in combined_df.columns:
            combined_df[col] = None

    # Reorder columns
    combined_df = combined_df[list(column_mapping.values())]

    # Save the combined DataFrame to a single CSV file
    combined_df.to_csv('combined_earthquake_data.csv', index=False)

    print("Combined data has been successfully saved to 'combined_earthquake_data.csv'")

    # Delete individual CSV files
    csv_files = [
        'riseq_earthquake_data.csv',
        'earthquaketrack_earthquake_data.csv',
        'isr_earthquake_data.csv',
        'earthquakelist_earthquake_data.csv'
    ]
    for file in csv_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted {file}")

if __name__ == "__main__":
    run_scrapers_and_combine()