import pandas as pd

pesos = pd.read_csv('../../data/pesos_vegetales.csv', index_col = False)
bedca = pd.read_csv('../../data/bedca.csv')
recipes = pd.read_csv('../../data/output.csv',sep='|')

def fill_grams(df):
    '''
    NaN weight values filler function.
        -The ingredients present in the weights dataset are substituted accordingly.
        -For the remaining ingredients: weight(ingredient) = mean(weight(ingredient))
    '''
    df['Index'] = df.index
    original_columns = list(df.columns)
    
    weights = df[df['Unidad']=='None']
    weights = pd.merge(weights, pesos, how='inner', on='Ingrediente')

    weights['Grams'] = weights['Peso x Unidad']
    weights['Unidad'] = 'unidad'
    weights['Total_Grams'] = weights['Grams'].multiply(weights['Cantidad'], axis = 'index')
    
    # replacing new weights in original df
    weights = weights[original_columns]
    weights.set_index(weights['Index'], inplace=True)
    result = df.copy()
    result.loc[weights['Index'],:] = weights

    #n comensales
    result = pd.merge(result,recipes['Num_comensales'], how='left', left_on='Recipe_id', right_index=True)
    result['Num_comensales'] = result['Num_comensales'].fillna(1)
    result['Total_Grams'] = result['Total_Grams'].divide(result['Num_comensales']).round(5)
    
    # mean values for remaining ingredients + drop na
    result[['Grams','Total_Grams']] = result.groupby(['Ingrediente'])[['Grams','Total_Grams']].transform(lambda x: x.fillna(x.mean()).round())
    na_count = result['Total_Grams'].isna().groupby(result['Recipe_id']).sum()
    missing = list(na_count[na_count != 0].index)
    result = result[~result['Recipe_id'].isin(missing)]
    
    return result.drop(['Index'], axis=1)

def drop_evaluation(original,result):
    original_recipes = original['Recipe_id'].unique()
    result_recipes = result['Recipe_id'].unique()
    print(f'{len(original_recipes)-len(result_recipes)} recipes dropped:')
    dropped_recipe_ids = list(set(original_recipes) - set(result_recipes))
    print(dropped_recipe_ids)

if __name__ == "__main__":
    ing = pd.read_csv('../../data/ingredientes.csv',sep = '|')
    result = fill_grams(ing)
    drop_evaluation(ing,result)
    result.to_csv('../../data/ingredients_100.csv',index=False)