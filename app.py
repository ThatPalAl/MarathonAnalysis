import os
from flask import Flask, render_template
from map import generate_marathon_map
from plotting import (
    plot_race_times_hist,
    plot_race_time_categories,
    plot_age_vs_time,
    histogram_pace,
    pace_categories_perKM,
    pace_pie_chart,
    age_v_time,
    pace_chart
)

app = Flask(__name__)

WORKOUT_MAPS_DIR = 'static/images/workout_maps'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/my_marathons.html')
def my_marathons():
    marathon_map = generate_marathon_map()  
    
    plot_race_times_hist()
    plot_race_time_categories()
    plot_age_vs_time()
    histogram_pace()
    pace_categories_perKM()
    pace_pie_chart()
    age_v_time()
    pace_chart()

    return render_template('marathon_map.html')  


@app.route('/my_trainings')
def my_trainings():
    workout_files = [f for f in os.listdir(WORKOUT_MAPS_DIR) if f.endswith('.html')]
    
    
    buttons = []
    for workout_file in workout_files:
        # Extract the workout name from the file name (e.g., "Run_2024-09-15_10.23km")
        workout_name = workout_file.replace('_', ' ').replace('.html', '')
        button_html = f'<a href="/{WORKOUT_MAPS_DIR}/{workout_file}" target="_blank"><button>{workout_name}</button></a>'
        buttons.append(button_html)
    return render_template('my_trainings.html', buttons=buttons)


if __name__ == '__main__':
    app.run(debug=True)
