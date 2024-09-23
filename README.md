<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>EarthquakeScraper Project</h1>

<div class="section">
    <h2>Overview</h2>
    <p>This project scrapes earthquake data from multiple sources and combines them into a single CSV file. The sources include:</p>
    <ul>
        <li><a href="https://earthquakelist.org/india/">Earthquake List</a></li>
        <li><a href="https://isr.gujarat.gov.in/latest-earthquakes-reports">ISR (Institute of Seismological Research)</a></li>
        <li><a href="https://riseq.seismo.gov.in/">RISEQ (Regional Integrated Multi-Hazard Early Warning System)</a></li>
        <li><a href="https://earthquaketrack.com/recent">Earthquake Track</a></li>
    </ul>
</div>

<div class="section">
    <h2>Project Structure</h2>
    <p>The project consists of the following files:</p>
    <ul>
        <li><code>run_scrapers.py</code>: The main script that runs all scrapers and combines the data.</li>
        <li><code>scrape_earthquakelist.py</code>: Scrapes data from Earthquake List.</li>
        <li><code>scrape_isr.py</code>: Scrapes data from ISR.</li>
        <li><code>scrape_riseq.py</code>: Scrapes data from RISEQ.</li>
        <li><code>scrape_earthquaketrack.py</code>: Scrapes data from Earthquake Track.</li>
    </ul>
</div>

<div class="section">
    <h2>Setup and Installation</h2>
    <p>To set up and run the project, follow these steps:</p>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/Ashwintomar/EarthquakeScraper.git</code></pre>
        <li>Navigate to the project directory:</li>
        <pre><code>cd EarthquakeScraper</code></pre>
        <li>Install the required Python packages:</li>
        <pre><code>pip install requests beautifulsoup4 pandas</code></pre>
        <li>Run the main script:</li>
        <pre><code>python run_scrapers.py</code></pre>
    </ol>
</div>

<div class="section">
    <h2>File Descriptions</h2>
    <h3><code>run_scrapers.py</code></h3>
    <p>This script runs all the scrapers and combines the data into a single CSV file. It also adds source information to each DataFrame and processes the data to ensure consistency.</p>
    <h3><code>scrape_earthquakelist.py</code></h3>
    <p>This script scrapes earthquake data from the Earthquake List website and saves it to a CSV file.</p>
    <h3><code>scrape_isr.py</code></h3>
    <p>This script scrapes earthquake data from the ISR website and saves it to a CSV file.</p>
    <h3><code>scrape_riseq.py</code></h3>
    <p>This script scrapes earthquake data from the RISEQ website and saves it to a CSV file.</p>
    <h3><code>scrape_earthquaketrack.py</code></h3>
    <p>This script scrapes earthquake data from the Earthquake Track website and saves it to a CSV file.</p>
</div>

<div class="section">
    <h2>How It Works</h2>
    <p>The project works as follows:</p>
    <ol>
        <li><strong>Scraping Data:</strong> Each scraper script (e.g., <code>scrape_earthquakelist.py</code>) sends a GET request to the respective website, parses the HTML content using BeautifulSoup, and extracts the required earthquake data.</li>
        <li><strong>Saving Data:</strong> The extracted data is saved to individual CSV files (e.g., <code>earthquakelist_earthquake_data.csv</code>).</li>
        <li><strong>Combining Data:</strong> The <code>run_scrapers.py</code> script loads each CSV file into a DataFrame, adds source information, and processes the data to ensure consistency across all sources.</li>
        <li><strong>Output:</strong> The combined data is saved to a single CSV file named <code>combined_earthquake_data.csv</code>.</li>
    </ol>
</div>

<div class="section">
    <h2>Dependencies</h2>
    <p>The project relies on the following Python packages:</p>
    <ul>
        <li><code>requests</code>: For sending HTTP requests to the websites.</li>
        <li><code>beautifulsoup4</code>: For parsing HTML content.</li>
        <li><code>pandas</code>: For data manipulation and CSV file handling.</li>
    </ul>
</div>

<div class="section">
    <h2>Contributing</h2>
    <p>Contributions to the project are welcome! If you find any issues or want to add new features, please submit a pull request.</p>
</div>

<div class="section">
    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>
</div>

<div class="section">
    <h2>Contact</h2>
    <p>For any questions or feedback, please contact the project maintainer at <a href="mailto:ashwintomar04@gmail.com">ashwintomar04@gmail.com</a>.</p>
</div>

</body>
</html>
