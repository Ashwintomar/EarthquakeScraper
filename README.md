---

# 🌍 EarthquakeScraper Project

This project scrapes earthquake data from multiple sources and combines them into a single CSV file. 

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [File Descriptions](#file-descriptions)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🌐 Overview

This project scrapes earthquake data from multiple sources and combines them into a single CSV file. The sources include:

- [Earthquake List](https://earthquakelist.org/india/)
- [ISR (Institute of Seismological Research)](https://isr.gujarat.gov.in/latest-earthquakes-reports)
- [RISEQ (Regional Integrated Multi-Hazard Early Warning System)](https://riseq.seismo.gov.in/)
- [Earthquake Track](https://earthquaketrack.com/recent)

---

## 📁 Project Structure

The project consists of the following files:

- **`run_scrapers.py`**: The main script that runs all scrapers and combines the data.
- **`scrape_earthquakelist.py`**: Scrapes data from Earthquake List.
- **`scrape_isr.py`**: Scrapes data from ISR.
- **`scrape_riseq.py`**: Scrapes data from RISEQ.
- **`scrape_earthquaketrack.py`**: Scrapes data from Earthquake Track.

---

## ⚙️ Setup and Installation

To set up and run the project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ashwintomar/EarthquakeScraper.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd EarthquakeScraper
    ```

3. **Install the required Python packages:**

    ```bash
    !pip install requests beautifulsoup4 pandas
    ```

4. **Run the main script:**

    ```bash
    python run_scrapers.py
    ```

---

## 📄 File Descriptions

### `run_scrapers.py`

This script runs all the scrapers and combines the data into a single CSV file. It adds source information to each DataFrame and processes the data to ensure consistency.

### `scrape_earthquakelist.py`

This script scrapes earthquake data from the Earthquake List website and saves it to a CSV file.

### `scrape_isr.py`

This script scrapes earthquake data from the ISR website and saves it to a CSV file.

### `scrape_riseq.py`

This script scrapes earthquake data from the RISEQ website and saves it to a CSV file.

### `scrape_earthquaketrack.py`

This script scrapes earthquake data from the Earthquake Track website and saves it to a CSV file.

---

## 🛠️ How It Works

1. **Scraping Data**: Each scraper script (e.g., `scrape_earthquakelist.py`) sends a GET request to the respective website, parses the HTML content using BeautifulSoup, and extracts the required earthquake data.
2. **Saving Data**: The extracted data is saved to individual CSV files (e.g., `earthquakelist_earthquake_data.csv`).
3. **Combining Data**: The `run_scrapers.py` script loads each CSV file into a DataFrame, adds source information, and processes the data to ensure consistency across all sources.
4. **Output**: The combined data is saved to a single CSV file named `combined_earthquake_data.csv`.

---

## 📦 Dependencies

The project relies on the following Python packages:

- **`requests`**: For sending HTTP requests to the websites.
- **`beautifulsoup4`**: For parsing HTML content.
- **`pandas`**: For data manipulation and CSV file handling.

---

## 🤝 Contributing

Contributions are welcome! If you find any issues or want to add new features, please submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 📬 Contact

For any questions or feedback, please contact the project maintainer at [ashwintomar04@gmail.com](mailto:ashwintomar04@gmail.com).

---
