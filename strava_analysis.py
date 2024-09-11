import os
import json
import polyline
import folium
from datetime import datetime

save_directory = 'static/images/workout_maps'
save_file_name = 'activities_data.json'

def load_activities():
    with open(save_file_name, 'r') as f:
        activities = json.load(f)
    return activities


def filter_run_activities(activities):
    return [activity for activity in activities if 'Run' in activity['name']]


# using folium map with each workout coordinates to save every run as a separate map (if it's accessible) 
# and display it on the trainings subpage
def plot_activity_map(activity, save_directory):
    if activity['map'] and activity['map']['summary_polyline']:
        polyline_str = activity['map']['summary_polyline']
        coordinates = polyline.decode(polyline_str)

        map_center = coordinates[0] if coordinates else [0, 0]
        activity_map = folium.Map(location=map_center, zoom_start=13)


        folium.PolyLine(coordinates, color="blue", weight=2.5, opacity=1).add_to(activity_map)

    

        distance_km = activity['distance'] / 1000
        distance_str = f"{distance_km:.2f}km"

        activity_date = datetime.strptime(activity['start_date'], "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d')

        map_name = f"Run_{activity_date}_{distance_str}.html"
        map_path = os.path.join(save_directory, map_name)

        activity_map.save(map_path)
        print(f"Map for {activity['name']} saved as {map_path}")

        return map_name
    else:
        print(f"No map data available for {activity['name']}")
        return None


#button for each workout - specific name config
def format_button_html(activity, map_name):
    date = datetime.strptime(activity['start_date'], "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d')
    distance_km = activity['distance'] / 1000 
    button_html = f'''
    <a href="/static/images/workout_maps/{map_name}" target="_blank">
        <button class="run-button">Run {distance_km:.2f} km on {date}</button>
    </a>
    '''
    return button_html

def analyze_activities():
    

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    activities = load_activities()
    run_activities = filter_run_activities(activities)

    buttons_html = ''

    for activity in run_activities:
        print(f"Name: {activity['name']}, Distance: {activity['distance']}")
        map_name = plot_activity_map(activity, save_directory)
        if map_name:
            buttons_html += format_button_html(activity, map_name)

    with open('templates/run_buttons.html', 'w') as f:
        f.write(buttons_html)
        print('Run buttons HTML written to templates/run_buttons.html')


if __name__ == '__main__':
    analyze_activities()
