import pandas as pd
from geopandas.tools import geocode

# Function to load data from a CSV file


def load_data(filename, sep=",", encoding='utf-8'):
    """
    Loads data from a CSV file into a DataFrame.

    Args:
        filename (str): Path to the CSV file.
        delimiter (str, optional): Delimiter character in the CSV file. Defaults to ','.
        encoding (str, optional): Encoding of the CSV file. Defaults to 'utf-8'.

    Returns:
        pandas.DataFrame: DataFrame with loaded data.
    """
    df = pd.read_csv(filename, sep=sep, encoding=encoding)
    return df

# Function to geocode addresses


def geocode_addresses(df, provider="arcgis", user_agent=None, timeout=None):
    """
    Geocodes addresses in a DataFrame, adding a column with coordinates.

    Args:
        df (pandas.DataFrame): DataFrame with addresses.
        provider (str, optional): Name of the geocoding provider. Defaults to 'arcgis'.
        user_agent (str, optional): User agent for requests to the geocoder.
        timeout (int, optional): Timeout for requests to the geocoder (in seconds).

    Returns:
        pandas.DataFrame: DataFrame with added coordinates.
    """
    addresses = df[["address", "city", "district", "neighbourhoods"]].apply(
        lambda x: ', '.join(x.dropna()), axis=1)
    geocoded_df = geocode(addresses, provider=provider,
                          user_agent=user_agent, timeout=timeout)
    geocoded_df.columns = ['coordinates', 'full_address']
    # geocoded_df['coordinates'] = geocoded_df['coordinates'].apply(lambda geom: f"{geom.y:.6f},{geom.x:.6f}")
    return geocoded_df

# Function to save geocoded data to a CSV file


def save_data(df, output_filename):
    """
    Saves a DataFrame with geocoded data to a CSV file.

    Args:
        df (pandas.DataFrame): DataFrame with geocoded data.
        output_filename (str): Path to the output CSV file.
    """
    df.to_csv(output_filename, index=False)

# Main function that combines all steps


def main(input_filename, output_filename, sep=",", provider="arcgis", encoding='utf-8'):
    """
    Loads data from CSV, geocodes addresses, and saves the result to CSV.

    Args:
        input_filename (str): Path to the input CSV file.
        output_filename (str): Path to the output CSV file.
        delimiter (str, optional): Delimiter character in the CSV file. Defaults to ','.
        provider (str, optional): Name of the geocoding provider. Defaults to 'arcgis'.
        encoding (str, optional): Encoding of the CSV file. Defaults to 'utf-8'.
    """
    df = load_data(input_filename, sep, encoding)
    geocoded_df = geocode_addresses(df, provider)
    df = df.join(geocoded_df, how='left')
    save_data(df, output_filename)


# Example usage
if __name__ == "__main__":
    main(r"geocoder\data\address_test.csv", r"geocoder\data\output_test.csv")
