from flask import Flask
from flask import jsonify
from flask import render_template
import altair as alt

app = Flask(__name__)

cars = alt.load_dataset('cars')

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    achart = create_chart()
    return render_template('index.html', title='Home', user=user, altairchart = achart)

@app.route('/test')
def test():
    cjson = create_chart
    return jsonify(cjson)

def create_chart():
    c = alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    )
    cjson = c.to_dict()
    return cjson


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')