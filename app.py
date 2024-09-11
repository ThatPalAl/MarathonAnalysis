from flask import Flask, render_template
from map import generate_marathon_map

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/my_marathons')
def my_marathons():
    marathon_map = generate_marathon_map()  
    return render_template('marathon_map.html', marathon_map=marathon_map)

@app.route('/my_trainings')
def my_trainings():
    return "<h2>Trainings will be available soon!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
