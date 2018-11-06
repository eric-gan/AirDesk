
from flask import Flask, render_template, request #imports flask and flask CORS (this allows us to make our
from flask_cors import CORS #server)
from find_closest_spaces import find_closest, get_user_location
import json
# from find_closest_spaces import find_closest
app = Flask(__name__) #initializes the app

CORS(app) #allows cross-origin sharing (meaning anyone can send requests to the app)
counter = 0 #this makes counter global (we need this so that when a user changes counter it persists and doesn't get set back to 0 every time).
@app.route('/', methods=['GET'])
def index():  # pragma: no cover #this loads index.html as the primary web page
    return render_template('index.html')

@app.route('/explore', methods=['GET'])
def explore():  # pragma: no cover #this loads index.html as the primary web page
	loc = request.args.get('address', default = '', type = str)
	dic = get_user_location(loc)
	geocode = dic['lat'], dic['lng']
	return render_template('index2.html', geocode=geocode)
@app.route('/addspace', methods=['GET'])

if __name__ == "__main__":
    app.run(debug=True)