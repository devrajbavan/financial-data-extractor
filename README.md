# Revenue Extractor

A Python-based tool designed to extract and filter financial data for companies within a specific country. It leverages the **EODHD** API for retrieving stock tickers and **Yahoo Finance** for validating tickers and extracting detailed financial information.

## Features

- **Ticker Retrieval**: Fetches stock tickers for a specified country using the EODHD API.
- **Validation**: Verifies tickers against Yahoo Finance to ensure data availability.
- **Revenue Filtering**: Filters companies based on a minimum revenue threshold (default: 10M).
- **Data Extraction**: Extracts key company details including:
  - Name, HQ Location, Market Cap
  - Current Price, Previous Close, Volume
  - Company Description, Sector, Industry
  - Total Branches (Employees)
- **Excel Output**: Saves the filtered and extracted data into an `output.xlsx` file.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **EODHD API Key**: You need an API key from [EODHD](https://eodhd.com/).

## Installation

1.  **Clone the repository** (or download the source code).

2.  **Install dependencies**:
    Navigate to the project directory and run:
    ```bash
    pip install -r requirments.txt
    ```
    *(Note: The requirements file is named `requirments.txt`)*

## Configuration

Before running the script, you need to configure a few settings in `scrapper.py`:

1.  Open `scrapper.py` in a text editor or IDE.
2.  **Set your API Key**:
    Find the `API_KEY` variable and replace the placeholder with your actual EODHD API key.
    ```python
    API_KEY = "YOUR_EODHD_API_KEY"
    ```
3.  **Set the Target Country**:
    Update the `COUNTRY` variable to your desired country.
    ```python
    COUNTRY = "denmark"  # Example: "usa", "germany", "india"
    ```
    *Refer to `exchange.py` for a list of supported countries and their mapping.*
4.  **Set Minimum Revenue**:
    Adjust the `MIN_REVENUE` threshold as needed.
    ```python
    MIN_REVENUE = 10_000_000
    ```

## Usage

Run the main script:

```bash
python scrapper.py
```

### Workflow
1.  The script fetches raw tickers from EODHD for the configured country.
2.  It iterates through each ticker, converting it to a Yahoo Finance format (using `suffixes.py`).
3.  It checks if the company has valid financial data on Yahoo Finance.
4.  It checks if the "Total Revenue" exceeds the `MIN_REVENUE` threshold.
5.  If criteria are met, it extracts full company details.
6.  Finally, it saves all data to `output.xlsx`.

## Output

The script generates an `output.xlsx` file in the same directory containing the extracted data for qualifying companies.

## Project Structure

-   `scrapper.py`: Main script containing the logic for fetching, validating, and extracting data.
-   `exchange.py`: Mapping of country names to EODHD exchange codes and Yahoo Finance suffixes.
-   `suffixes.py`: Mapping of country names to specific Yahoo Finance suffixes.
-   `requirments.txt`: List of Python dependencies required for the project.

## Troubleshooting

-   **"EODHD did NOT return JSON"**: Check your API key and ensure you haven't hit your rate limit.
-   **"No Yahoo match found"**: Some tickers from EODHD might not have a direct equivalent on Yahoo Finance or might use a different suffix not covered in `suffixes.py`.
