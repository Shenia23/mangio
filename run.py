from flask import Flask, render_template, jsonify
from random import *
import json 
from flask_cors import CORS, cross_origin
import requests

from app.recommender.recommender import getRecommendation

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, support_credentials=True, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/recomendacion', methods=['GET'])
@cross_origin()
def get_recomendacion():
    data = getRecommendation()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
