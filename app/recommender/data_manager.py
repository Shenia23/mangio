import pandas as pd
import numpy as np

from config import recipes, ingredients, nvalues

wanted_columns = ['Id','Categoria','Nombre','Dificultad','Tipo']
macros = ['energia','grasa','proteina','fibra','carbohidratos','Recipe_id']

def recipes2dict(recommendations):
    '''
    :param recommendations: dict with recipe recommendation ids and type of food
                            example: {74146: 'comida', 19602: 'snack']}

    :return recom: dictionary containing all the relevant information regarding the recipes
    '''
    recom = recipes[recipes.Id.isin(recommendations)].replace(np.nan,None)
    ing = ingredients[ingredients['Recipe_id'].isin(recommendations)].replace(np.nan,None)

    recom = recom[wanted_columns]
    recom['Comida'] = recom['Id'].apply(lambda x: recommendations[x]) # set type of food
    recom = recom.merge(nvalues[macros], left_on='Id', right_on='Recipe_id') # add nutritional values
    recom.drop(['Recipe_id'],axis=1,inplace=True)
    recom = recom.to_dict('records')

    # append ingredients
    for recipe in recom:
        recipe['Ingredientes'] =  ing[ing['Recipe_id']==recipe['Id']].set_index('Recipe_id').to_dict('records')
    
    return recom