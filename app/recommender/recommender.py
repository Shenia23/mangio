import pandas as pd
import json
from random import randint

from config import recipes
from app.recommender.data_manager import recipes2dict

FOOD_CAT = ['Plato principal','Entrante','Acompñamiento','Cena']
SNACK_CAT = ['Merienda','Cumpleaños','Postre']
BREAKFAST_CAT = ['Desayuno']

class Recommender:

    def __init__(self):
        self.categories= {'Desayuno': BREAKFAST_CAT,
                    'Comida': FOOD_CAT,
                    'Snack': SNACK_CAT
                    }

    def recommend(self):
        '''
        :return: ids y tipo de comida recomendada, posible formato de recomendación final
        '''

        recommendation_ids = {self.getRandomByCategory('Snack'): 'merienda', 
                            self.getRandomByCategory('Snack'): 'snack', 
                            self.getRandomByCategory('Snack'):'snack', 
                            self.getRandomByCategory('Comida'): 'comida', 
                            self.getRandomByCategory('Desayuno'): 'desayuno', 
                            self.getRandomByCategory('Comida'): 'cena'}
        return recommendation_ids
    
    def getRandomByCategory(self, category):
        selected_category = recipes[recipes['Tipo'].isin(self.categories[category])]
        return int(selected_category['Id'].sample(n=1))
        

def getRecommendation():
    '''
    Método conectado con Flask, se instancia el recomendador (habria que ver dónde conviene hacer eso) 
    y se obtienen las recomendaciones
    '''
    recommender = Recommender()
    recommendation_ids = recommender.recommend()

    return recipes2dict(recommendation_ids)