from utils import *
from equivalences import equivalences


bedca = pd.read_csv('../../data/bedca.csv',index_col=0)
categorical_columns = ['nombre','categoria']
bedca_columns = list(bedca.drop(columns=categorical_columns).columns)

def nutri_value_extractor(ingredients):
    '''
    :param ingredients: df of recipes
    
    :return nutritional_values: df of nutritional values of each recipe
    '''
    join = pd.merge(ingredients, bedca, left_on="Indice", right_on='indice')
    join[bedca_columns] = join[bedca_columns].multiply(join['Total_Grams']/100, axis='index')
    bedca_columns.append('Recipe_id')
    nutritional_values = join[bedca_columns].groupby('Recipe_id').sum().round(6)
    nutritional_values['Gramos'] = join['Total_Grams'].sum()

    return nutritional_values


if __name__ == "__main__":
    ingredients = pd.read_csv('../../data/ingredients_100.csv')
    nutritional_values = nutri_value_extractor(ingredients)
    nutritional_values.to_csv('../../data/nutritional_values.csv', index=True)