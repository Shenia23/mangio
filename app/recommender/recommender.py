import pandas as pd
import json

from config import recipes
from app.recommender.data_manager import recipes2dict

class Recommender:

    def __init__(self):
        pass 

    def recommend(self):
        '''
        :return: ids y tipo de comida recomendada, posible formato de recomendación  "final", por ahora devuelve ids estáticas
        '''
        recommendation_ids = {74146: 'merienda', 
                            19602: 'snack', 
                            58107:'snack', 
                            64737: 'comida', 
                            50719: 'desayuno', 
                            45889: 'cena'}
        return recommendation_ids

def getRecommendation():
    '''
    Método conectado con Flask, se instancia el recomendador (habria que ver dónde conviene hacer eso) 
    y se obtienen las recomendaciones
    '''
    recommender = Recommender()
    recommendation_ids = recommender.recommend()

    return recipes2dict(recommendation_ids)