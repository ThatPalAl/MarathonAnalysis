import folium
from geopy.distance import geodesic


# Cooridnates of the route
coordinates = [
    (52.244214, 21.047115),
    (52.247613, 21.045669),
    (52.248158, 21.039446),
    (52.251310, 21.035515),
    (52.248353, 21.029077),
    (52.248113, 21.029040),
    (52.247739, 21.030080),
    (52.244522, 21.035233),
    (52.244026, 21.037454),
    (52.243286, 21.038635),
    (52.241867, 21.039182),
    (52.240709, 21.040630),
    (52.235756, 21.045343),
    (52.235024, 21.046395),
    (52.226721, 21.054045),
    (52.224906, 21.056278),
    (52.223264, 21.059698),
    (52.221607, 21.067551),
    (52.221396, 21.078667),
    (52.220922, 21.083731),
    (52.219303, 21.092155),
    (52.217705, 21.096941),
    (52.215181, 21.100889),
    (52.211797, 21.104885),
    (52.211836, 21.105186),
    (52.214926, 21.101430),
    (52.217345, 21.097783),
    (52.218988, 21.094135),
    (52.220097, 21.089208),
    (52.220636, 21.089509),
    (52.221214, 21.090582),
    (52.227550, 21.093897),
    (52.228161, 21.090979),
    (52.228306, 21.089681),
    (52.228049, 21.087792),
    (52.228213, 21.085775),
    (52.227872, 21.084464),
    (52.227294, 21.083810),
    (52.226004, 21.083662),
    (52.226164, 21.079568),
    (52.225832, 21.075495),
    (52.224957, 21.071265),
    (52.226981, 21.064374),
    (52.227502, 21.063739),
    (52.232347, 21.060782),
    (52.231594, 21.055890),
    (52.237494, 21.052209),
    (52.238029, 21.052278),
    (52.238438, 21.053412),
    (52.241976, 21.070529),
    #(52.242138, 21.071476),
    #(52.242207, 21.071408),
    (52.240700, 21.063957),
    (52.238531, 21.053331),
    (52.238385, 21.051392),
    (52.237864, 21.051415),
    (52.237520, 21.049314),
    (52.236804, 21.046002),
    (52.235561, 21.046615),
    (52.235506, 21.045934),
    (52.236839, 21.044369),
    (52.240138, 21.041420),
    (52.241117, 21.040355),
    (52.242075, 21.039141),
    (52.243589, 21.038597),
    (52.243686, 21.038472),
    (52.243888, 21.039674),
    (52.243902, 21.041557),
    (52.244443, 21.042702),
    (52.244922, 21.043031),
    (52.247714, 21.043269),
    (52.247707, 21.043507),
    (52.244929, 21.043258),
    (52.244228, 21.042736),
    (52.243971, 21.043076),
    (52.243207, 21.042849),
    (52.242985, 21.044210),
    (52.243103, 21.044698),
    (52.243503, 21.044738)
]

# # markers for each coordinate (for route improvement only)
# for i, coord in enumerate(coordinates):
#     if i % 5 == 0:
#         folium.Marker(
#             location=coord, 
#             popup=f"ID: {i+1}", 
#             icon=folium.Icon(color='blue')
#         ).add_to(map)


def calculate_total_distance(coords):
    total_distance = 0
    for i in range(1, len(coords)):
        total_distance += geodesic(coords[i-1], coords[i]).km
    return total_distance

#positionining on the route
def find_position_on_route(coords, checkpoint_km):
    cumulative_distance = 0
    for i in range(1, len(coords)):
        segment_distance = geodesic(coords[i-1], coords[i]).km
        cumulative_distance += segment_distance
        if cumulative_distance >= checkpoint_km:
            return coords[i]
    return coords[-1]

def generate_marathon_map():
    checkpoints = [5, 10, 15, 16.5, 20, 21.0975] #according to datasport resources
    start_location = [52.246450, 21.046131]
    map = folium.Map(location=start_location, zoom_start=13)

    #Checkpoints
    for checkpoint in checkpoints:
        position = find_position_on_route(coordinates, checkpoint)
        folium.Marker(location=position, popup=f"{checkpoint} km").add_to(map)

    # drawing polyline on th emap
    folium.PolyLine(locations=coordinates, color='blue', weight=5, opacity=0.8).add_to(map)

    #start and finish markers
    folium.Marker(location=coordinates[0], popup="Start", icon=folium.Icon(color='green')).add_to(map)
    folium.Marker(location=coordinates[-1], popup="Finish", icon=folium.Icon(color='red')).add_to(map)

    return map._repr_html_()  