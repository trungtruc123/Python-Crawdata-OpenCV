import folium

lat = 20.97
long = 105.8
zoom = 12

gmap2 = folium.Map(location=(lat, long), zoom_start=zoom)
gmap2.save('initialFolium.html')
