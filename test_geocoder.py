# import unittest
import pandas as pd
from geocoder import load_data, geocode_addresses, save_data

try:
    print(load_data(r'geocoder\address_test.csv'))
    print('\n\n', 130 * '_')
except:
    print('ERROR')

try:
    print(geocode_addresses(pd.read_csv(r'geocoder\address_test.csv')))
    print('\n\n', 130 * '_')
except:
    print('ERROR')