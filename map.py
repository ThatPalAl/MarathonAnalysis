import folium

#provide more specific coordinates later
coordinates = [
    (52.246450, 21.046131),
    (52.247613, 21.045669),
    (52.248106, 21.039689),
    (52.251310, 21.035515),
    (52.248075, 21.028960),
    (52.243679, 21.038166),
    (52.226721, 21.054045),
    (52.217611, 21.097028),
    (52.211862, 21.105068),
    (52.220183, 21.089082),
    (52.227557, 21.093652),
    (52.227425, 21.083996),
    (52.224967, 21.071100),
    (52.227097, 21.064190),
    (52.232306, 21.060749),
    (52.231583, 21.055835),
    (52.237760, 21.052187),
    (52.242175, 21.071542),
    (52.238509, 21.052938),
    (52.236525, 21.046200),
    (52.235342, 21.046158),
    (52.243423, 21.038647),
    (52.247759, 21.043368),
    (52.244204, 21.042670),
    (52.243193, 21.042885),
    (52.243055, 21.044666),
    (52.244493, 21.044741)
]

#adjusting zoom and map starting position
start_location = [52.246450, 21.046131]
map = folium.Map(location=start_location, zoom_start=13)

# line of the map - connect all coordinates
folium.PolyLine(locations=coordinates, color='blue', weight=5, opacity=0.8).add_to(map)

#markers for start and end
folium.Marker(location=coordinates[0], popup="Start", icon=folium.Icon(color='green')).add_to(map)
folium.Marker(location=coordinates[-1], popup="Finish", icon=folium.Icon(color='red')).add_to(map)

map.save('half_marathon_route.html')

