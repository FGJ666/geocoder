# import unittest
import pandas as pd
from geocoder import load_data, geocode_addresses, save_data

# class TestGeocoder(unittest.TestCase):

#     def test_load_data(self):
#         # Arrange
#         filename = "test_data.csv"
#         delimiter = ";"
#         expected_df = pd.DataFrame({"Город": ["Москва"], "Район": ["Центральный"], "Микрорайон": ["1-й"], "Адрес": ["ул. Ленина, 1"]})

#         # Act
#         df = load_data(filename, delimiter)

#         # Assert
#         pd.testing.assert_frame_equal(df, expected_df)

#     def test_geocode_addresses(self):
#         # Arrange
#         df = pd.DataFrame({"Город": ["Москва"], "Район": ["Центральный"], "Микрорайон": ["1-й"], "Адрес": ["ул. Ленина, 1"]})
#         provider = "arcgis"
#         expected_df = df.copy()
#         expected_df["geometry"] = "POINT (37.617733 55.755826)"  # Replace with expected geometry

#         # Act
#         geocoded_df = geocode_addresses(df, provider)

#         # Assert
#         pd.testing.assert_frame_equal(geocoded_df, expected_df)

#     def test_save_data(self):
#         # Arrange
#         df = pd.DataFrame({"Город": ["Москва"], "Район": ["Центральный"], "Микрорайон": ["1-й"], "Адрес": ["ул. Ленина, 1"]})
#         filename = "test_output.csv"

#         # Act
#         save_data(df, filename)

#         # Assert
#         # Check if the file exists and has the correct content (you might need to read the file and compare)
#         # ... (Implementation depends on how you want to verify the saved data)

# if __name__ == '__main__':
#     unittest.main()

df = pd.DataFrame({"city": ["boston"], "district": ["ma"], "neighbourhoods": [""], "address": ["1600 pennsylvania ave. washington, dc"]})
# print(geocode_addresses(df))

print(merge_addresses(df, geocode_addresses(df)))