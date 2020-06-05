import folium
import pandas
data = pandas.read_csv('volcanoes.csv')
volcanLat = list(data['Latitude'])
volcanLon =list(data['Longitude'])
volcaName =['Bufumbira',
 'Bunyaruguru Field',
 'Mount Elgon',
 'Fort Portal Field',
 'Mount Katunga',
 'Katwe Kikorongo Field',
 'Kyatwa Volcanic Field',
 'Mount Muhavura']
feet = [8005, 5098, 14178, 5000, 5600, 3501, 4692, 13450]
def color_producer(val):
    if val <= 5000:
        return 'green'
    elif val <= 10000:
        return 'yellow'
    else:
        return 'red'
map = folium.Map([1.3733,32.2903],width="97%",height="97%", zoom_start="7")

v = folium.FeatureGroup(name="volcanoes")
for na,la,lo,fe in zip(volcaName,volcanLat,volcanLon,feet):
    v.add_child(folium.CircleMarker(location=[la,lo],popup="{},{}ft".format(na,fe) ,radius=7,color='grey',fill_color=color_producer(fe), fill_opacity=0.7))

p = folium.FeatureGroup(name="population")
p.add_child(folium.GeoJson(data = open('world.json',mode='r',encoding="utf-8-sig").read(),
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(p)
map.add_child(v)
map.add_child(folium.LayerControl(position='topright',collapsed=True,))
map.save("myMap.Html")
