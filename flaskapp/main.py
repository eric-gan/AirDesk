
from flask import Flask, render_template #imports flask and flask CORS (this allows us to make our
from flask_cors import CORS #server)
app = Flask(__name__) #initializes the app

CORS(app) #allows cross-origin sharing (meaning anyone can send requests to the app)
counter = 0 #this makes counter global (we need this so that when a user changes counter it persists and doesn't get set back to 0 every time).
@app.route('/', methods=['GET'])
def index():  # pragma: no cover #this loads index.html as the primary web page
    return render_template('index.html')

@app.route('/explore', methods=['GET'])
def explore():  # pragma: no cover #this loads index.html as the primary web page
    return render_template('index2.html')
# @app.route('/counter', methods=['GET']) #this creates a route called /counter that we can reference in the front end called /counter and makes it a get method
# def get_counter(): #this function returns counter as a string
#         global counter
#         return str(counter), 200
# @app.route('/add', methods=['POST'])#this creates a route that we can reference in the front end called /add and makes it a post method
# def add_1(): #adds one to counter (remember this doesn't display counter, the         front-end needs to deal with this
#         global counter
#         counter = counter + 1
#         return '', 200
# @app.route('/subtract', methods=['POST'])
# def subtract_1(): #subtracts one from counter (also doesn't display counter)
#         global counter
#         counter = counter - 1
#         return '', 200