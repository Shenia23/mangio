from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import requests

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/recomendacion', methods=['GET'])
def get_recomendacion():
    recomendacion = [
        {
        'nombre': 'Receta de croquetas de pollo caseras de la abuela',
        'tipo': 'Desayuno',
        'calorias': 200,
        },
        {
        'nombre': 'Receta2',
        'tipo': 'Comida',
        'calorias': 354,
        }
    ]
    print('[INFO] answering: ', jsonify(recomendacion))
    return jsonify(recomendacion)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
