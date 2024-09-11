from flask import Flask, render_template
from map import generate_marathon_map
import os
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/my_marathons')
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

    return render_template('marathon_map.html', marathon_map=marathon_map)

@app.route('/my_trainings')
def my_trainings():
    return "<h2>This part of the website is still in development!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
