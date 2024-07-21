# import unittest
import pandas as pd
from geocoder import load_data, geocode_addresses, save_data

print(geocode_addresses(pd.read_csv(r'geocoder\address_test.csv')))