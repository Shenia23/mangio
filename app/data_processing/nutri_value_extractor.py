from utils import *
from equivalences import equivalences


testing_recipes = [74146, 73727, 74020 , 73919, 73818, 73799,73756, 73360, 73314, 73269, 72692, 72311, 72126,66092, 65997, 71629]

categorical_columns = ['nombre','categoria']
ingredients = pd.read_csv('../../data/bedca.csv',index_col=0)
ingredients_names = ingredients["nombre"].tolist()
ingredients['Id'] = ingredients.index
all_ingredients = ingredients_to_plural(ingredients_names)  # ingredientes originales + plurales
bedca_ingredients = [x.lower() for x in all_ingredients]


def extract_recipe_value(ingredients):
    '''
    :return result_df: df which contains the nutritional values of the total serving 
    '''
    nutri_values = get_df_by_ids(ingredients['Indice']).drop(columns = categorical_columns)
    nutri_columns = nutri_values.columns
    join = ingredients.join(nutri_values, on = 'Indice')
    join[nutri_columns] = join[nutri_columns].multiply(join['Total_Grams']/100, axis='index')
    result_df = join[nutri_columns].sum().round(6)
    result_df['Gramos'] = join['Total_Grams'].sum()

    return result_df
    
def get_df_by_ids(ids):
    ids = [i for i in ids if i != None]
    return ingredients[ingredients['Id'].isin(ids)]

def remove_list(row):
    '''
    function to remove lists from df
    '''
    if isinstance(row,list):
        row = row[0]
    return row

def get_grams(row):
    '''
    Function to change units to grams
    '''
    row = equivalences[row] 
    return row

def test():
    '''
    Demo para 1 receta con ingredientes bien extraidos
    '''
    df = pd.read_csv('../../data/output.csv', sep='|')
    recipes = df[["Id","Ingredientes"]].copy()
    recipes = recipes[recipes['Id'].isin(testing_recipes)]
    recipes.reset_index(drop=True, inplace=True)



    ing = recipes['Ingredientes'].iloc[0] #
    parsed_ingredients,_,_,_ = parse_ingredient_string(ing, bedca_ingredients)
    test = pd.DataFrame(parsed_ingredients)
    test = test.drop([1,3,4,10])
    test['Cantidad'] = test['Cantidad'].apply(remove_list)
    test['Cantidad'] = test['Cantidad'].astype(float)
    test['Ingrediente'] = test['Ingrediente'].apply(remove_list)
    test['Unidad'] = test['Unidad'].apply(remove_list)
    test['Indice'] = [243,419,22,507,907,483,404]

    test['Grams'] = test['Unidad'].apply(get_grams)
    test['Total_Grams'] = test['Grams'] * test['Cantidad']
    print('Test dataframe:')
    print(test)

    result = extract_recipe_value(test) #TODO meterlo en un bucle para todas las recetas
    print('Nutritional values')
    print(result)

if __name__ == "__main__":
    test()