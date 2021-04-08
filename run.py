from flask import Flask, render_template, jsonify, request
from random import *
import json 
from flask_cors import CORS, cross_origin
import requests
from app.user.user import User, createNewUser
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

@app.route('/recomendacion', methods=['GET','POST'])
@cross_origin()
def get_recomendacion():
    user = request.get_json()
    data = getRecommendation(user['username'])
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/newUser', methods=['POST'])
@cross_origin()
def create_user():
    
    '''Crea un nuevo usuario del sistema y almacena sus datos en un JSON'''
    print("User creation")
    print ("Is request json: ", request.is_json)
    new_user_data = request.get_json()
    print ("JSON content: ",new_user_data)

    new_user = createNewUser(new_user_data)
    
    new_user_json = json.dumps(new_user.__dict__)

    print("NEW USER CLASS: ", new_user_json)
    return 'JSON posted'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
