from flask import Flask
from flask import request
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/weather")
def get_weather():
    zip = request.args.get('zip')
    ''' This is a test account, otherwise including API Key is not recommended '''
    resp = requests.get('http://api.weatherapi.com/v1/current.json?key=d3910ad8104341f5b13144742201906&q=' + zip)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /weather/ {}'.format(resp.status_code))

    data = json.dumps(resp.json(), indent=2)
    return data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
