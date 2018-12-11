from flask import Flask
from flask import jsonify
from flask import render_template
import altair as alt
from vega_datasets import data

app = Flask(__name__)

cars = alt.load_dataset('cars')
source = data.barley()

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
    cjson = create_chart()
    return jsonify(cjson)

@app.route('/testdata')
def testdata():
    return jsonify(source.to_dict('records'))

def create_chart():
    c=alt.Chart(source).mark_bar().encode(
        x='yield:Q',
        y='year:O',
        color='year:N',
        row='site:N',
        tooltip=['yield', 'year']
    )
    cjson = c.to_dict()
    return cjson


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')