import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_isr():
    # URL of the website
    url = "https://isr.gujarat.gov.in/latest-earthquakes-reports"

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table with the class "views-table cols-9"
        table = soup.find('table', {'class': 'views-table cols-9'})

        # Extract the table headers
        headers = []
        for th in table.find_all('th'):
            headers.append(th.text.strip())

        # Extract the table rows
        rows = []
        for tr in table.find_all('tr')[1:]:  # Skip the header row
            row = []
            for td in tr.find_all('td'):
                row.append(td.text.strip())
            rows.append(row)

        # Convert the data into a pandas DataFrame
        df = pd.DataFrame(rows, columns=headers)

        # Drop the "Action" column
        df = df.drop(columns=['Action'])

        # Save the DataFrame to a CSV file
        df.to_csv('isr_earthquake_data.csv', index=False)
        print("Data has been successfully scraped and saved to 'isr_earthquake_data.csv'")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")