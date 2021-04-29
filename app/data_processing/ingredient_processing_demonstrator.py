# %%
import pandas as pd
import pattern as es
import nltk
from nltk.stem import WordNetLemmatizer
import re
import numpy as np
import os
import sys
module_path = os.path.abspath(os.path.join('../..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from app.data_processing.utils import measure_average_rate
from app.data_processing.utils import filter_ingredient_100
from app.data_processing.utils import extract_ingredients_to_csv
from app.data_processing.weight_filler import fill_grams, append_category
from app.data_processing.weight_filler import drop_evaluation

# %%
def nutri_value_extractor(ingredients):
    '''
    :param ingredients: df of recipes
    
    :return nutritional_values: df of nutritional values of each recipe
    '''
    join = pd.merge(ingredients, bedca, left_on="Indice", right_on='indice')
    join[bedca_columns] = join[bedca_columns].multiply(join['Total_Grams']/100, axis='index')
    bedca_columns.append('Recipe_id')
    bedca_columns.append('Total_Grams')
    nutritional_values = join[bedca_columns].groupby('Recipe_id').sum().round(6)

    return nutritional_values
# %%
bedca = pd.read_csv('../../data/bedca.csv',index_col=0)
recipes = pd.read_csv('../../data/filtered_recipes.csv', sep='|')
recipes_for_demonstration = pd.read_csv('../../data/ingredient_filtering_demonstration.csv', sep='|')