import folium
map = folium.Map(location = [48, 68], zoom_start = 5) #coordinates of kasachstan

fg = folium.FeatureGroup(name = "My Map")
#fg.add_child(folium.GeoJSON())
coordinates = [
    [49,69],
    [50,78],
    [51,50],
    [49,74.3]
]

names = [
    'Coordinate 1',
    'Astana',
    'Copper Mine',
    'Oil Rig'
]

def color_producer(number):
    if number%2 == 0:
        return 'green'
    else:
        return 'blue'
for i in range(len(coordinates)):
    map.add_child(folium.Marker(location = coordinates[i], popup = names[i], icon = folium.Icon(color = color_producer(i))))
map.add_child(fg)
map.save("karte.html")