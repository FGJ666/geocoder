import pandas as pd
from geopandas.tools import geocode

# Функция для загрузки данных из CSV файла
def load_data(filename, delimiter=";"):
    return pd.read_csv(filename, delimiter=delimiter)

# Функция для геокодирования адресов
def geocode_addresses(df, provider="arcgis"):
    addresses = geocode((df["city"] + ", " + df["district"] + ", " + 
                         df["neighbourhoods"] + ", " + df["address"]), 
                         provider=provider, user_agent=None, timeout=None)
    return addresses

# Функция для сохранения геокодированных данных в CSV файл
def save_data(df, geocod_data):
    geocoded_addresses = df.join(geocod_data, how="inner", rsuffix="_geocode")
    df.to_csv(geocoded_addresses, index=False)

# Основная функция, объединяющая все шаги
def main(input_filename, output_filename, delimiter=";", provider="arcgis"):
    df = load_data(input_filename, delimiter)
    geocoded_df = geocode_addresses(df, provider)
    df = merge_addresses(df, geocoded_df)
    save_data(geocoded_df, output_filename)