import pandas as pd
import numpy as np
import json
import time
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler
from random import randint

from config import recipes, ingredients, nvalues, combined
from app.user.user import getUser
from app.recommender.recom_constants import *
from app.recommender.data_manager import recipes2dict

recipe_nvalues = pd.merge(recipes, nvalues, on='Recipe_id', how='right')
recipe_nvalues = recipe_nvalues.set_index('Recipe_id', drop=False)
recipe_nvalues.index.name = 'index'

comb_scaler = StandardScaler()
recipe_scaler = StandardScaler()

combined[TARGET_MACROS] = comb_scaler.fit_transform(combined[TARGET_MACROS])

scaled_recipes = recipe_nvalues.copy()
scaled_recipes[TARGET_MACROS] = recipe_scaler.fit_transform(recipe_nvalues[TARGET_MACROS])

# TODO filtrado extra para que no recomiende comidas de 100 kcal y cenas de 1000 kcal 
# TODO implementar que se envíen recetas similares

class Recommender:

    def __init__(self, tdee, objective, preferences=None):
        self.tdee = tdee
        self.calories = {
            BREAKFAST:  self.tdee * 0.2,
            SNACK:      self.tdee * 0.1,
            MERIENDA:   self.tdee * 0.1,
            LUNCH:      self.tdee * 0.35,
            DINNER:     self.tdee * 0.25
        }
        self.objective = objective
        self.preferences = preferences
        self.iterations = ITERATIONS
        self.alpha = 0.7
        

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

        recom['nutritional_score'] = 0
        recom['preference_score'] = 0
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
        eucl_dist = Recommender.get_euclidean_distances([target_values[TARGET_MACROS]], combined, comb_scaler)
        lowest_indexes = np.argpartition(eucl_dist, 20)

        lowest_score_combinations = pd.DataFrame()
        for index in lowest_indexes[:20]:
            combined_ids = combined.loc[index, ['Recipe1','Recipe2']].to_list()
            combined_recom = recipe_nvalues.loc[combined_ids].copy()
            combined_recom['iteration'] = index
            combined_recom['nutritional_score'] = eucl_dist[index]/2
            lowest_score_combinations = lowest_score_combinations.append(combined_recom)

        best_combination = self.select_best_recom(lowest_score_combinations, calculate_nutritional_score=False).copy()
        best_combination['Comida'] = LUNCH
        best_combination.at[best_combination[KCAL].idxmin(),['Comida']] = DINNER

        return best_combination

    def select_best_recom(self, recom, calculate_nutritional_score = True):
        '''
        Escoge la mejor recomendación diaria entre varias:
         1. Calcula la score de preferencias
         2. Calcula la score nutricional
         3. Calcula la score pondrada combinada y escoge la mínima
        '''

        recom['preference_score'] = recom.index.to_series().apply(Recommender.get_preferences_score, preferences=self.preferences)

        columns = TARGET_MACROS.copy()
        columns += ['iteration','preference_score','nutritional_score']
        daily_recom = recom[columns].groupby('iteration').sum()
        
        if calculate_nutritional_score:
            target_macros = pd.Series(get_macro_objectives(self.tdee, self.objective))
            daily_recom['nutritional_score'] = Recommender.get_euclidean_distances([target_macros], daily_recom, StandardScaler(), scale_df=True)

        daily_recom['combined_score'] = self.get_combined_score(daily_recom['preference_score'].values, daily_recom['nutritional_score'].values)
        best_iteration = daily_recom['combined_score'].idxmin()

        if calculate_nutritional_score:
            print(daily_recom)
            print('Best iteration:', best_iteration)

        return recom[recom['iteration'] == best_iteration]

    def most_similar(self, recipe, n=1):
        '''
        Devuelve las recetas más similares
        '''
        eucl_dist = Recommender.get_euclidean_distances(recipe, scaled_recipes, recipe_scaler)

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

    def get_combined_score(self, preference_scores, nutritional_scores):
        '''
        Calcula la score ponderada a partir de las scores nutricional y de gustos
            1. Pondera la score de gustos para que esté en la misma escala que la nutricional
            2. combined score = alpha*nutri_score - (1-alpha)*recom_score, donde alpha > 0.5
        '''
        max_range = nutritional_scores.max()
        scaled_preferences = Recommender.sigmoid(preference_scores, max_range=max_range)
        return self.alpha*nutritional_scores-(1-self.alpha)*scaled_preferences

    @staticmethod
    def sigmoid(x, max_range):
        '''
        Función sigmoide usada para ponderar la score de gustos.
        Parameros de la función sigmoide:
            sigmoid_range: valores máximo y mínimo (límites horizontales), rango de la función
            center: -0.5 para que pase por 0
            curve: 1.5 para que tienda a width/-width a partir de 2/-2 (valores "grandes" de la score de gustos)
        '''
        sigmoid_range = max_range * 2
        center = 0.5
        curve = -1.5

        sigmoid = ( ( 1/(1+np.e**(curve*x)) ) - center ) * sigmoid_range
        return sigmoid

    @staticmethod
    def get_euclidean_distances(target, df, scaler, scale_df=False):
        '''
        Devuelve las distancias euclidianas escalando si hace falta
        '''
        if scale_df:
            scaled_df = df.copy()
            scaled_df[TARGET_MACROS] = scaler.fit_transform(df[TARGET_MACROS])
        else:
            scaled_df = df
        
        scaled_target = scaler.transform(target)
        eucl_dist = euclidean_distances(scaled_target, scaled_df[TARGET_MACROS].values).reshape(-1)

        return eucl_dist

    @staticmethod   
    def get_preferences_score(recipe_id, preferences):
        '''
        Devuelve la score de preferencias de una receta
            1. Calcula la score de cada ingrediente individual según su categoría
            2. La score de la receta es su suma
        '''
        ing_rec = ingredients[ingredients['Recipe_id']==recipe_id].copy()
        ing_rec['score'] = ing_rec['Category'].apply(lambda category: preferences.get(category, 0))
        return ing_rec['score'].sum()

    @staticmethod
    def filter_by_range(df, column, values):
        filtered_df = df[df[column].between(left=values[0], right=values[1])]
        return filtered_df

def getRecommendation(username):
    '''
    Método conectado con Flask, se instancia el recomendador a partir de los datos de usuario
    y se obtienen las recomendaciones
    '''
    print("Recommendation for ",username)
    start = time.time()
    recommender = create_recommender(getUser(username))
    recommendation = recommender.recommend()
    end = time.time()
    print("Recommendation time: ", end-start)
    return recipes2dict(recommendation)

def create_recommender(user): 
    '''
    :param user: es un dict con la info sacada del json correspondiente 
    Método para crear recommender a partir de un perfil de usuario 
    '''
    preferences = {'Carne': 1.05, 
                    'Pollo': 0.3333333333333333, 
                    'Pescado': 0.3666666666666667, 
                    'Legumbres': 0.8833333333333334, 
                    'Verduras': -0.4, 'Patatas': 0.275, 'Arroz': 0.0, 'Pasta': 0.25, 
                    'Huevos': -0.5833333333333333}

    recommender = Recommender(
                    tdee = user['tdee'],
                    objective = user['objective'],
                    preferences = preferences #TODO coger preferencias del usuario
                  )

    return recommender