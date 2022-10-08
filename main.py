from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

#this route("/") is what the user will open on the browser
@app.route("/")
def index():
    #displaying all the data
    return jsonify({
        'data': data,
        'message': 'success'
    }), 200

@app.route('/planet')

#this is returning the data for one planet at a time
def planet():
    #fetching name of the planet from the url
    name = request.args.get('name')
    #using next() we are finding a dictionary that satisfies the condition (the name should match whatever you are entering)
    #if name is matching it will return the same information
    planet_data = next(item for item in data if item['name'] == name)
    return jsonify({
        'data': planet_data,
        'message': 'success'
    }), 200

if __name__ == "__main__":
    app.run()