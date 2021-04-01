import pandas as pd
import json
from random import randint

from config import recipes
from app.recommender.data_manager import recipes2dict

class Recommender:

    def __init__(self):
        pass 

    def recommend(self):
        '''
        :return: ids y tipo de comida recomendada, posible formato de recomendación  "final", por ahora devuelve ids estáticas
        '''
        random_ids = []
        for i in range(6):
            random_index = randint(1,len(recipes))
            random_ids.append( recipes['Id'][random_index] )

        recommendation_ids = {random_ids[0]: 'merienda', 
                            random_ids[1]: 'snack', 
                            random_ids[2]:'snack', 
                            random_ids[3]: 'comida', 
                            random_ids[4]: 'desayuno', 
                            random_ids[5]: 'cena'}
        return recommendation_ids

def getRecommendation():
    '''
    Método conectado con Flask, se instancia el recomendador (habria que ver dónde conviene hacer eso) 
    y se obtienen las recomendaciones
    '''
    recommender = Recommender()
    recommendation_ids = recommender.recommend()

    return recipes2dict(recommendation_ids)