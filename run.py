from flask import Flask, render_template, request
import datetime, requests

app = Flask(__name__)
baseurl = 'http://10.1.0.110:8080/movies/name/'

@app.route("/")
def index():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/details")
def details():
    name = request.args.get('name', default = '*', type = str)
    print(name)
    fullurl = baseurl + name
    response = requests.get(fullurl)
    movie = response.json()
    print(movie)
    return render_template('details.html', movie=movie)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
 