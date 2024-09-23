import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_riseq():
    # URL of the webpage containing the earthquake data
    url = 'https://riseq.seismo.gov.in/'

    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all earthquake event items
    event_items = soup.find_all('li', class_='list-view-item event_list')

    # Initialize lists to store the extracted data
    event_ids = []
    event_names = []
    origin_times = []
    lat_longs = []
    magnitude_depths = []
    event_types = []

    # Extract data from each event item
    for item in event_items:
        event_id = item['data-json'].split('"event_id":"')[1].split('"')[0]
        event_name = item['data-json'].split('"event_name":"')[1].split('"')[0]
        origin_time = item['data-json'].split('"origin_time":"')[1].split('"')[0]
        lat_long = item['data-json'].split('"lat_long":"')[1].split('"')[0]
        magnitude_depth = item['data-json'].split('"magnitude_depth":"')[1].split('"')[0]
        event_type = item['data-json'].split('"event_type":"')[1].split('"')[0]

        event_ids.append(event_id)
        event_names.append(event_name)
        origin_times.append(origin_time)
        lat_longs.append(lat_long)
        magnitude_depths.append(magnitude_depth)
        event_types.append(event_type)

    # Create a DataFrame from the extracted data
    data = {
        'Event ID': event_ids,
        'Event Name': event_names,
        'Origin Time': origin_times,
        'Latitude, Longitude': lat_longs,
        'Magnitude, Depth': magnitude_depths,
        'Event Type': event_types
    }

    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('riseq_earthquake_data.csv', index=False)

    print("Data has been successfully scraped and saved to 'riseq_earthquake_data.csv'")