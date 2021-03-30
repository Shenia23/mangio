import pandas as pd

recipes = pd.read_csv('data/output.csv', sep='|')
ingredients = pd.read_csv('data/ingredients_100.csv')
nvalues = pd.read_csv('data/nutritional_values.csv')