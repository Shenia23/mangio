import pandas as pd
import numpy as np
import json
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler
from random import randint

from config import recipes, nvalues, combined
from app.user.user import getUser
from app.recommender.recom_constants import *
from app.recommender.data_manager import recipes2dict

recipe_nvalues = pd.merge(recipes, nvalues, on='Recipe_id', how='right')

scaler = StandardScaler()

combined[TARGET_MACROS] = scaler.fit_transform(combined[TARGET_MACROS])

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
        :return recom: df con las recetas a recomendar
        '''
        recom = pd.DataFrame()

        # recomendación fijada de desayuno y snacks
        for type in FIXED_FOOD_TYPES:
            selected_recipe = self.get_fixed_recommendation(type)
            selected_recipe['Comida'] = type
            recom = recom.append(selected_recipe)

        #recomendación combinada de comida y cena
        target_values = self.get_missing_macros(recom)
        combined_recom = self.get_combined_recommendation(target_values)
        recom = recom.append(combined_recom)

        return recom
    
    def get_fixed_recommendation(self, type):
        '''
        Pasos:
            1. Filtrado por categorías
            2. Filtrado por porcentaje de kcal
            3. Selección aleatoria

        :param type: tipo de comida a recomendar (desayuno, merienda, snack)
        :return selected_recipe: receta recomendada
        '''
        calories = self.calories[type]
        selected_category = recipe_nvalues[recipe_nvalues['Tipo'].isin(CATEGORIES[type])]
        filtered_calories = Recommender.filter_by_range(
                                        df=selected_category,
                                        column='energia',
                                        values=[calories*0.9, calories*1.1]
                                    )
        
        selected_recipe = filtered_calories.sample(n=1)
        return selected_recipe
    
    def get_combined_recommendation(self, target_values):
        '''
        Usa la distancia euclidiana para encontrar los valores más cercanos a los target_values

        :param target_values: gramos restantes de cada macro tras haber fijado las meriendas y desayunos
        :return combined_recom: df formada por la mejor combinación de comida y cena
        '''
        scaled_targets = scaler.transform([target_values[TARGET_MACROS]])
        eucl_dist = euclidean_distances(scaled_targets, combined[TARGET_MACROS].values).reshape(-1)
        min_ed_index = (np.where(eucl_dist == np.amin(eucl_dist)))[0]

        combined_ids = list(combined[['Recipe1','Recipe2']].iloc[min_ed_index[0]])

        combined_recom = recipe_nvalues[recipe_nvalues['Recipe_id'].isin((combined_ids))].reset_index().copy()
        # TODO asignar comida y cena en funcion de kcal
        combined_recom['Comida'] = LUNCH
        combined_recom.at[1,'Comida'] = DINNER
        return combined_recom

    def get_missing_macros(self, fixed_df):
        '''
        :param fixed_df: df con los valores que ya se han recomendado
        :return missing: df con las cantidades de macros que faltan por recomendar
        '''
        total = fixed_df[TARGET_MACROS].sum()

        macros_mean = dict()
        for macro, value in MACROS.items():
            macros_mean[macro] = np.mean(value[self.objective])*value[CAL_GRAM]
        macros_mean[KCAL] = self.tdee

        missing = pd.Series(macros_mean)-total
        
        return missing
    
    @staticmethod
    def filter_by_range(df, column, values):
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
    recommendation = recommender.recommend()

    return recipes2dict(recommendation)

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