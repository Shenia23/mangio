import pandas as pd
import numpy as np

pesos = pd.read_csv('../../data/pesos_vegetales.csv', index_col = False)
bedca = pd.read_csv('../../data/bedca.csv')
recipes = pd.read_csv('../../data/output.csv',sep='|')

def fill_grams(df):
    '''
    NaN weight values filler function.
        -The ingredients present in the weights dataset are substituted accordingly.
        -For the remaining ingredients: weight(ingredient) = mean(weight(ingredient))
    '''
    result = df.copy()
    result['Index'] = df.index
    original_columns = list(result.columns)

    result['Grams'] = result['Grams'].replace(0,np.nan)
    weights = result[result['Grams'].isna()]

    weights = pd.merge(weights, pesos, how='inner', on='Ingrediente')

    weights['Grams'] = weights['Peso x Unidad']
    weights['Unidad'] = 'unidad'
    weights['Total_Grams'] = weights['Grams'].multiply(weights['Cantidad'], axis = 'index')
    
    # replacing new weights in original df
    weights = weights[original_columns]
    weights.set_index(weights['Index'], inplace=True)
    result.loc[weights['Index'],:] = weights

    #n comensales
    result = pd.merge(result,recipes['Num_comensales'], how='left', left_on='Recipe_id', right_index=True)
    result['Num_comensales'] = result['Num_comensales'].fillna(1)
    result['Total_Grams'] = result['Total_Grams'].divide(result['Num_comensales']).round(5)
    # TODO poner GRAMOS por PERSONA en otra columna (ajustar nutri_value_extractor tambien)
    
    # mean values for remaining ingredients + drop na
    result[['Grams','Total_Grams']] = result.groupby(['Ingrediente'])[['Grams','Total_Grams']].transform(lambda x: x.fillna(x.mean()).round(5))
    na_count = result['Grams'].isna().groupby(result['Recipe_id']).sum()
    missing = list(na_count[na_count != 0].index)
    result = result[~result['Recipe_id'].isin(missing)]
    
    return result.drop(['Index'], axis=1)

def getBedcaCategory(row):
    cat = bedca['categoria'][bedca['indice']==row]
    return cat.values[0]

def append_category(df):
    df['Category'] = df['Indice'].apply(getBedcaCategory)

def drop_evaluation(original,result):
    original_recipes = original['Recipe_id'].unique()
    result_recipes = result['Recipe_id'].unique()
    print(f'{len(original_recipes)-len(result_recipes)} recipes dropped:')
    dropped_recipe_ids = list(set(original_recipes) - set(result_recipes))
    print(dropped_recipe_ids)

if __name__ == "__main__":
    ing = pd.read_csv('../../data/ingredientes.csv')
    result = fill_grams(ing)
    append_category(result)
    drop_evaluation(ing,result)
    result.to_csv('../../data/ingredients_100.csv',index=False)