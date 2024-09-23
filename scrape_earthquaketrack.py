import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape_earthquaketrack():
    # URL of the website
    url = "https://earthquaketrack.com/recent"

    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all earthquake entries
    quake_entries = soup.find_all('div', class_='quake-info-container')

    # List to store the extracted data
    earthquake_data = []

    # Loop through each earthquake entry and extract the required information
    for entry in quake_entries:
        quake_info = {}
        
        # Extract magnitude
        magnitude_span = entry.find('span', class_='text-warning') or entry.find('span', class_='text-muted')
        quake_info['Magnitude'] = magnitude_span.text.strip() if magnitude_span else 'N/A'
        
        # Extract depth
        depth_text = entry.text.split(',')[-1].strip()
        quake_info['Depth'] = depth_text.split(' ')[0] if 'depth' in depth_text else 'N/A'
        
        # Extract location
        location_links = entry.find_all('a', href=True)
        if location_links:
            # Concatenate the text from all location links, excluding those with date and time
            quake_info['Location'] = ', '.join([link.text.strip() for link in location_links if not link.text.strip().startswith('Today') and not link.text.strip().startswith('2024-')])
        else:
            quake_info['Location'] = 'N/A'
        
        # Extract time
        time_abbr = entry.find('abbr', class_='timeago')
        quake_info['Time'] = time_abbr['datetime'] if time_abbr else 'N/A'
        
        # Extract URL
        quake_url = entry.find('a', href=True)
        quake_info['URL'] = quake_url['href'] if quake_url else 'N/A'
        
        # Append the extracted data to the list
        earthquake_data.append(quake_info)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(earthquake_data)

    # Save the DataFrame to a CSV file
    df.to_csv('earthquaketrack_earthquake_data.csv', index=False)

    print("Earthquaketrack data has been successfully saved to 'earthquaketrack_earthquake_data.csv'")

if __name__ == "__main__":
    scrape_earthquaketrack()