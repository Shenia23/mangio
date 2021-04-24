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

comb_scaler = StandardScaler()
recipe_scaler = StandardScaler()

combined[TARGET_MACROS] = comb_scaler.fit_transform(combined[TARGET_MACROS])

scaled_recipes = recipe_nvalues.copy()
scaled_recipes[TARGET_MACROS] = recipe_scaler.fit_transform(recipe_nvalues[TARGET_MACROS])

# TODO filtrado extra para que no recomiende comidas de 100 kcal y cenas de 1000 kcal 
# TODO implementar que se envíen recetas similares

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
        self.iterations = 5
        

    def recommend(self):
        '''
        :return recom: df con las recetas a recomendar
        '''
        recom = pd.DataFrame()

        for i in range(self.iterations):
            # recomendación fijada de desayuno y snacks
            day = self.get_daily_recommendation()
            day['iteration'] = i
            recom = recom.append(day)
    
        recom.reset_index(inplace=True)
        best_recom = self.select_best_recom(recom)

        return best_recom

    def get_daily_recommendation(self):
        '''
        Devuelve una recomandación para un día
        '''
        # recomendación fijada de desayuno y snacks
        day = pd.DataFrame()
        for type in FIXED_FOOD_TYPES:
            selected_recipe = self.fixed_recommendation(type)
            selected_recipe['Comida'] = type
            day = day.append(selected_recipe)

        #recomendación combinada de comida y cena
        combined_recom = self.combined_recommendation(self.get_missing_macros(day))
        day = day.append(combined_recom)

        return day
    
    def fixed_recommendation(self, type):
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
                                        column=KCAL,
                                        values=[calories*0.9, calories*1.1]
                                    )
        
        selected_recipe = filtered_calories.sample(n=1)
        return selected_recipe
    
    def combined_recommendation(self, target_values):
        '''
        Usa la distancia euclídea para encontrar los valores más cercanos a los target_values
        La receta con más kcal es la comida, y la que tiene menos la cena. 

        :param target_values: df gramos restantes de cada macro tras haber fijado las meriendas y desayunos
        :return combined_recom: df formada por la mejor combinación de comida y cena
        '''
        scaled_targets = comb_scaler.transform([target_values[TARGET_MACROS]])
        eucl_dist = euclidean_distances(scaled_targets, combined[TARGET_MACROS].values).reshape(-1)
        min_ed_index = (np.where(eucl_dist == np.amin(eucl_dist)))[0]

        combined_ids = list(combined[['Recipe1','Recipe2']].iloc[min_ed_index[0]])
        combined_recom = recipe_nvalues[recipe_nvalues['Recipe_id'].isin((combined_ids))].copy()
        
        combined_recom = combined_recom.sort_values(KCAL,ascending=False).reset_index()
        combined_recom['Comida'] = LUNCH
        combined_recom.at[1,'Comida'] = DINNER
        return combined_recom

    def select_best_recom(self, recom):
        '''
        Escoge la mejor recomendación diaria entre varias
        '''
        target_macros = pd.DataFrame(get_macro_objectives(self.tdee, self.objective), index=[1])
        columns = TARGET_MACROS.copy()
        columns.append('iteration')
        recom_macros = recom[columns].groupby('iteration').sum()

        scaler = StandardScaler()
        recom_macros[TARGET_MACROS] = scaler.fit_transform(recom_macros[TARGET_MACROS])
        target_macros = scaler.transform(target_macros)

        recom_macros['score'] = euclidean_distances(target_macros, recom_macros[TARGET_MACROS]).reshape(-1)
        best_iteration = recom_macros['score'].idxmin()

        return recom[recom['iteration'] == best_iteration]

    def most_similar(self, recipe, n=1):
        '''
        Devuelve las recetas más similares
        '''
        scaled_recipe = recipe_scaler.transform(recipe[TARGET_MACROS])
        eucl_dist = euclidean_distances(scaled_recipe, scaled_recipes[TARGET_MACROS]).reshape(-1)

        most_similar_indexes = np.argsort(eucl_dist)[:n]
        most_similar = recipe_nvalues.iloc[most_similar_indexes]

        return most_similar

    def get_missing_macros(self, fixed_df):
        '''
        :param fixed_df: df con los valores que ya se han recomendado
        :return missing: df con las cantidades de macros que faltan por recomendar
        '''
        total = fixed_df[TARGET_MACROS].sum()
        macros_goals = pd.Series(get_macro_objectives(self.tdee, self.objective))
        missing = macros_goals-total
        
        return missing

    def get_preferences_score(self, x=2):
        sigmoid = ((1/1+np.e**(-x/2)-0.5)*1.9)
        return sigmoid

    def get_combined_sore(self, recipe_df):
        return self.alpha*recipe_df['distance']-(1-self.alpha)*recipe_df['preferences_score']

    @staticmethod
    def filter_by_range(df, column, values):
        filtered_df = df[df[column].between(left=values[0], right=values[1])]
        return filtered_df

def getRecommendation(username):
    '''
    Método conectado con Flask, se instancia el recomendador a partir de los datos de usuario
    y se obtienen las recomendaciones
    '''
    print("username",username)
    user = getUser(username)
    recommender = create_recommender(user) #posible nuevo metodo getRecommender (if exists) con pickle
    print(f'Recommendation for user with tdee={recommender.tdee} and objective={recommender.objective}')
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
                    objective = user['objective']
                  )

    return recommender