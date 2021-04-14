import pandas as pd

recipes = pd.read_csv('data/filtered_recipes_100.csv', sep='|')
ingredients = pd.read_csv('data/ingredients_100.csv')
nvalues = pd.read_csv('data/nutritional_values.csv')
images = pd.read_csv('data/image_src.csv')
combined = pd.read_csv("data/combined.csv") 