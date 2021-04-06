import pandas as pd
import json
from random import randint

from config import recipes, nvalues
from app.recommender.data_manager import recipes2dict

# FOOD TYPES
BREAKFAST = 'desayuno'
LUNCH = 'comida'
DINNER = 'cena'
SNACK = 'snack'
MERIENDA = 'merienda'

recipe_nvalues = pd.merge(recipes, nvalues, on='Recipe_id', how='right')

class Recommender:

    def __init__(self, tdee):
        self.food_types = [BREAKFAST, LUNCH, DINNER, SNACK, MERIENDA]
        self.categories= {
                    BREAKFAST:  ['Desayuno'],
                    LUNCH:      ['Plato principal','Entrante','Acompañamiento'],
                    SNACK:      ['Merienda','Cumpleaños','Postre'],
                    MERIENDA:   ['Merienda','Cumpleaños','Postre'],
                    DINNER:     ['Cena']
                    }
        self.tdee = tdee
        self.calories = {
            BREAKFAST:  self.tdee * 0.2,
            SNACK:      self.tdee * 0.1,
            MERIENDA:   self.tdee * 0.1,
            LUNCH:      self.tdee * 0.35,
            DINNER:     self.tdee * 0.25
        }

    def recommend(self):
        '''
        :return: ids y tipo de comida recomendada, posible formato de recomendación final
        '''
        recommendations = dict()

        for type in self.food_types:
            recommendations[self.get_food(type)] = type

        return recommendations

    
    def get_food(self, type):
        '''
        :param type: tipo de comida a recomendar (desayuno, comida, cena...)
        :return recipe_id: id de la receta recomendada
        '''
        calories = self.calories[type]
        selected_category = recipe_nvalues[
                                (recipe_nvalues['Tipo'].isin(self.categories[type])) 
                                & (recipe_nvalues["energia"] > (calories*0.9) )
                                & (recipe_nvalues["energia"] < (calories * 1.1))
                            ]
        selected_recipe = selected_category.sample(n=1)
        
        return int(selected_recipe['Recipe_id'])

def getRecommendation():
    '''
    Método conectado con Flask, se instancia el recomendador (habria que ver dónde conviene hacer eso) 
    y se obtienen las recomendaciones
    '''
    tdee = 2500 # esto sería un param desde el perfil de usuario!
    recommender = Recommender(tdee)
    recommendation_ids = recommender.recommend()
    print('Recommendation: ', recommendation_ids)

    return recipes2dict(recommendation_ids)

def create_recommender(user_id):
    '''
    #TODO
    Método para crear recommender a partir de un perfil de usuario 
    '''
    recommender = Recommender()

    return recommender