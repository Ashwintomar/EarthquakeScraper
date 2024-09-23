import requests
from bs4 import BeautifulSoup
import csv

def scrape_earthquakelist():
    # URL of the webpage
    url = "https://earthquakelist.org/india/"

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table with the earthquake data
        table = soup.find('table', {'id': 'eq_wid_table_latest'})

        # Check if the table was found
        if table:
            # Open a CSV file to write the data
            with open('earthquakelist_earthquake_data.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write the header row
                writer.writerow(['Date and Time', 'Magnitude', 'Location'])

                # Find all rows in the table body
                rows = table.find_all('tr')

                # Iterate over each row (skip the header row)
                for row in rows[1:]:
                    # Find all cells in the row
                    cells = row.find_all('td')

                    # Extract the data from each cell
                    date_time = cells[0].get_text(strip=True)
                    magnitude = cells[1].get_text(strip=True)
                    location = cells[2].get_text(strip=True)

                    # Write the data to the CSV file
                    writer.writerow([date_time, magnitude, location])

            print("Data has been successfully scraped and saved to 'earthquakelist_earthquake_data.csv'")
        else:
            print("Table not found on the webpage.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")