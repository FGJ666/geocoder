import pandas as pd
import folium
from shapely import wkt

# Load data from CSV
df = pd.read_csv('geocoder/output_test.csv')

# Convert coordinates to geometric objects
df['geometry'] = df['coordinates'].apply(wkt.loads)

# Create an empty map
m = folium.Map()

# List to store all coordinates
coordinates = []

# Add markers for each location
for _, row in df.iterrows():
    point = row['geometry']
    coordinates.append([point.y, point.x])
    folium.Marker(
        location=[point.y, point.x],
        popup=f"{row['neighbourhoods']}, {row['city']}",
        tooltip=row['full_address']
    ).add_to(m)

# Adjust the map to make all markers visible
m.fit_bounds(coordinates)

# Save the map to an HTML file
m.save('map.html')
