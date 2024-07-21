# Geocoding Addresses README

## Overview
This project provides a set of Python functions to load address data from a CSV file, geocode the addresses to obtain their coordinates, and save the geocoded data back to a CSV file. The geocoding is performed using the `geopandas` library.

## Features
- Load address data from a CSV file into a Pandas DataFrame.
- Geocode addresses to get latitude and longitude coordinates.
- Save the geocoded data to a new CSV file.

## Requirements
- Python 3.6 or higher
- pandas
- geopandas

You can install the required libraries using pip:
```bash
pip install pandas geopandas
```

## Functions

### `load_data(filename, sep=",", encoding='utf-8')`
Loads data from a CSV file into a DataFrame.

**Arguments:**
- `filename` (str): Path to the CSV file.
- `sep` (str, optional): Delimiter character in the CSV file. Defaults to ','.
- `encoding` (str, optional): Encoding of the CSV file. Defaults to 'utf-8'.

**Returns:**
- `pandas.DataFrame`: DataFrame with loaded data.

### `geocode_addresses(df, provider="arcgis", user_agent=None, timeout=None)`
Geocodes addresses in a DataFrame, adding a column with coordinates.

**Arguments:**
- `df` (pandas.DataFrame): DataFrame with addresses.
- `provider` (str, optional): Name of the geocoding provider. Defaults to 'arcgis'.
- `user_agent` (str, optional): User agent for requests to the geocoder.
- `timeout` (int, optional): Timeout for requests to the geocoder (in seconds).

**Returns:**
- `pandas.DataFrame`: DataFrame with added coordinates.

### `save_data(df, output_filename)`
Saves a DataFrame with geocoded data to a CSV file.

**Arguments:**
- `df` (pandas.DataFrame): DataFrame with geocoded data.
- `output_filename` (str): Path to the output CSV file.

### Running the Script
To run the script, execute the following command in your terminal:
```bash
python your_script_name.py
```

Replace `your_script_name.py` with the name of your Python file.
