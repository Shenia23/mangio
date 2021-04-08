import pandas as pd
import json
from random import randint

from config import recipes, nvalues
from app.user.user import getUser
from app.recommender.recom_constants import *
from app.recommender.data_manager import recipes2dict

recipe_nvalues = pd.merge(recipes, nvalues, on='Recipe_id', how='right')

class Recommender:

    def __init__(self, tdee, objective):
        self.tdee = tdee
        self.calories = {
            BREAKFAST:  self.tdee * 0.2,
            SNACK:      self.tdee * 0.1,
            MERIENDA:   self.tdee * 0.1,
            LUNCH:      self.tdee * 0.35,
            DINNER:     self.tdee * 0.25
        }
        self.objective = objective

    def recommend(self):
        '''
        :return: ids y tipo de comida recomendada, posible formato de recomendación final
        '''
        recommendations = dict()

        for type in FOOD_TYPES:
            recommendations[self.get_food(type)] = type

        return recommendations

    
    def get_food(self, type):
        '''
        Pasos:
            1. Filtrado por categorías
            2. Filtrado por porcentaje de grasas, proteínas y carbohidratos
                (ahora hace esto para cada comida pero luego lo cambiamos por combinatoria etc)
            3. Selección aleatoria

        :param type: tipo de comida a recomendar (desayuno, comida, cena...)
        :return recipe_id: id de la receta recomendadad
        '''
        calories = self.calories[type]
        selected_category = recipe_nvalues[
                                (recipe_nvalues['Tipo'].isin(CATEGORIES[type])) 
                                & (recipe_nvalues["energia"].between(left=calories*0.9, right=calories*1.1))
                            ]
        
        accomplished_macros = selected_category
        for macro in MACROS.values():
            accomplished_macros = Recommender.filter_recipes_by_range(
                                        df=accomplished_macros,
                                        column=macro["column"],
                                        values=macro[self.objective]
                                    )
        
        try:                                
            selected_recipe = accomplished_macros.sample(n=1)
        except: #no quedan recetas después del segundo filtrado
            print("No recipes remaining after macro filtering for type: ",type)
            print("Selecting a random recipe instead")
            selected_recipe = selected_category.sample(n=1)

        return int(selected_recipe['Recipe_id'])
    
    @staticmethod
    def filter_recipes_by_range(df, column, values):
        filtered_df = df[df[column].between(left=values[0], right=values[1])]
        return filtered_df

def getRecommendation(username):
    '''
    Método conectado con Flask, se instancia el recomendador a partir de los datos de usuario
    y se obtienen las recomendaciones
    #TODO guardar recomendadores para cada user / tipo de user?
    '''
    user = getUser(username)
    recommender = create_recommender(user) #posible nuevo metodo getRecommender (if exists) con pickle
    recommendation_ids = recommender.recommend()

    return recipes2dict(recommendation_ids)

def create_recommender(user): 
    '''
    :param user: es un DICT con la info sacada del json correspondiente 
    #TODO devolver la clase User
    
    Método para crear recommender a partir de un perfil de usuario 
    '''
    recommender = Recommender(
                    tdee = user['tdee'],
                    objective = user['user_objective']
                  )

    return recommender