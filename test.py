import pandas as pd

new_recipe_data= {'creator': 'demo_3', 'recipe_name': 'Receta_demo', 
                  'ingredients': [{'name': 'Batido de chocolate', 'quantity': '100', 'unit': 'ml'}, 
                                  {'name': 'Arroz con leche', 'quantity': '11', 'unit': 'gr'}]}

all_ingredients = []
    
for ingredient in new_recipe_data["ingredients"]:
    ingredient_string = ingredient['quantity']+ " " + ingredient['unit'] + " " + ingredient['name'].lower()
    all_ingredients.append(ingredient_string)

user_recipes_df = pd.read_csv("./data/user_recipes.csv", usecols =["Creador","Nombre","Ingredientes"])


d = {'Creador': [new_recipe_data["creator"]], 'Nombre': [new_recipe_data["recipe_name"]], "Ingredientes" : [', '.join(all_ingredients)]}
new_recipe_df = pd.DataFrame(data=d)

print( new_recipe_df)


user_recipes_df = user_recipes_df.append(new_recipe_df)
print(user_recipes_df)
user_recipes_df.to_csv("./data/user_recipes.csv")