import pandas as pd
from utils import ingredients_to_plural, extract_ingredients_to_csv, ingredients_to_plural_dict
from weight_filler import fill_grams, append_category, drop_evaluation
from nutri_value_extractor import nutri_value_extractor
def ingredient_extraction():
    recipes = pd.read_csv('../../data/demo/ingredient_filtering_demonstration.csv', sep='|')
    recipes = recipes[recipes['Ingredientes'].notna()]
    recipes_ingredients = recipes[["Recipe_id", "Ingredientes"]].copy()

    ingredients = pd.read_csv('../../data/bedca.csv')
    bedca_ingredients = ingredients["nombre"].tolist()
    bedca_ingredients_lower = [x.lower() for x in bedca_ingredients]

    bedca_ingredients_lower_with_plurals = ingredients_to_plural(
        bedca_ingredients_lower)  # ingredientes originales + plurales
    bedca_ingredients_lower_plurals_dict = ingredients_to_plural_dict(
        bedca_ingredients_lower)

    recipes.reset_index(drop=True, inplace=True)
    # measure_average_rate(recipes)
    print("NUM_RECETAS: ", recipes_ingredients.shape[0])
    recipes_ingredients_df=extract_ingredients_to_csv(recipes)
    recipes_ingredients_df.to_csv('../../data/demo/ingredientes_demostracion.csv', index=False, header=True, sep=',')
    print("Ingredients extracted to: ../../data/demo/ingredientes_demostracion.csv")
    return

def weight_filling():
    ing = pd.read_csv('../../data/demo/ingredientes_demostracion.csv')
    result = fill_grams(ing)
    append_category(result)
    drop_evaluation(ing,result)
    result.to_csv('../../data/demo/ingredients_demostracion_filled.csv',index=False)
    print("Ingredients with filled weights stored in : ../../data/demo/ingredients_demostracion_filled.csv")
    
def nutritional_values():
    ingredients = pd.read_csv('../../data/demo/ingredients_demostracion_filled.csv')
    nutritional_values = nutri_value_extractor(ingredients)
    nutritional_values.to_csv('../../data/demo/nutritional_values_demostracion.csv', index=True)
    print("Nutritional values stored in: ../../data/demo/nutritional_values_demostracion.csv ")
    
if __name__ == "__main__":
    ingredient_extraction()
    weight_filling()
    nutritional_values()