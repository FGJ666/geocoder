import pandas as pd
import folium
from shapely import wkt

# Загрузить данные из CSV
df = pd.read_csv('geocoder/output_test.csv')

# Преобразовать координаты в геометрические объекты
df['geometry'] = df['coordinates'].apply(wkt.loads)

# Создать карту с центром на первых координатах
first_point = df['geometry'].iloc[0]
m = folium.Map(location=[first_point.y, first_point.x], zoom_start=4)

# Добавить маркеры для каждого места
for _, row in df.iterrows():
    point = row['geometry']
    folium.Marker(
        location=[point.y, point.x],
        tooltip=row['full_address']
    ).add_to(m)

# Сохранить карту в HTML файл
m.save(r'geocoder\map\map.html')
