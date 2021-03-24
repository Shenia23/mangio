import pandas as pd
import pattern.es as es
import nltk
from nltk.stem import WordNetLemmatizer
import re
import numpy as np


equivalences = {
    'kg': 1000,
    'kilos': 1000,
    'kilogramo': 1000,
    'kilogramos': 1000,
    'kilo': 1000,
    'kgr': 1000,
    'g': 1,
    'gr': 1,
    'grs': 1,
    'cucharillas': 5,
    'cucharaditas': 7,
    'cucharadas': 10,
    'cucharadas soperas': 17,
    'cucharadas de postre': 5,
    'cucharadas de postre': 5,
    'tazas': 150,
    'vasos': 250,
    'tarro': 250,
    'cuencos': 330,
    'envases': 0,
    'paquetes': 0,
    'bolsas': 0,
    'latas': 330,
    'botellas': 1000,
    'litros': 1000,
    'frascos': 30,
    'gotas': 0.003,
    'cabezas': 15,
    'pellizcos': 1,
    'sobres': 16,
    'dientes': 3,
    'puñados': 100,
    'barras': 250,
    'cajas': 43,
    'copas': 300,
    'pizcas': 1,
    'chorros': 2,
    'chorritos': 1,
    'unidades': 0,
    'unidad': 0,
    'racimos': 300,
    'lonchas': 17,
    'capas': 0,
    'rebanadas': 60,
    'gajos': 0,
    'tallos': 250,
    'cuadrados': 43,
    'ramas': 50,
    'ramitas': 40,
    'filetes': 140,
    'trozos': 100,
    'patas': 120,
    'muslos': 390,
    'cubos': 10,
    'tiras': 35,
    'bandejas': 430,
    'láminas': 410,
    'gramos': 1,
    'mililitros': 0.001,
    'cucharilla': 5,
    'cucharadita': 7,
    'cucharada': 10,
    'cucharada sopera': 17,
    'taza': 150,
    'vaso': 250,
    'cuenco': 330,
    'envase': 0,
    'paquete': 0,
    'bolsa': 0,
    'lata': 330,
    'botella': 1000,
    'litro': 1000,
    'frasco': 30,
    'gota': 0.003,
    'cabeza': 15,
    'pellizco': 1,
    'sobre': 16,
    'diente': 3,
    'puñado': 100,
    'barra': 250,
    'pechuga': 400,
    'copa': 300,
    'pizca': 1,
    'chorro': 2,
    'chorrito': 1,
    'racimo': 300,
    'loncha': 17,
    'capa': 0,
    'rebanada': 60,
    'gajo': 0,
    'tallo': 250,
    'cuadrado': 43,
    'rama': 50,
    'ramita': 40,
    'filete': 140,
    'trozo': 100,
    'pata': 120,
    'muslo': 390,
    'cubo': 10,
    'tira': 35,
    'bandeja': 430,
    'lámina': 410,  # de hojaldre 'hoja': 10,
    'gramo': 1,
    'mililitro': 0.001
}


def ingredients_to_plural_dict(ingredients_raw):

    ingredients_and_plurals_dict = {}
    # Add Pluralized bbc ingredients in order to catch ingredients like tomatoes, carrots, etc
    for ingredient in ingredients_raw:
        if len(ingredient.split(' ')) == 1:
            # añadimos a la lista los plurales de aquellos que sean una sola palabra
            ingredients_and_plurals_dict[ingredient] = es.pluralize(ingredient)
        else:
            ingredients_and_plurals_dict[ingredient] = ingredient
    return ingredients_and_plurals_dict


def ingredients_to_plural(ingredients_raw):
    # Add Pluralized bbc ingredients in order to catch ingredients like tomatoes, carrots, etc
    ingredients_plural = []
    for i in ingredients_raw:
        if len(i.split(' ')) == 1:
            # añadimos a la lista los plurales de aquellos que sean una sola palabra
            ingredients_plural.append(es.pluralize(i))
    ingredients_raw = ingredients_raw + ingredients_plural
    return ingredients_raw


def extract_n_grams(source, n_grams, standard_elements):

    tokens = nltk.word_tokenize(str(source))
    token_lower = [str.lower(i) for i in tokens]
    pairs = [" ".join(pair).replace("'", "")
             for pair in nltk.ngrams(token_lower, n_grams)]
    clean_pairs = [i for i in pairs if i in standard_elements]
    pairs_joined = []
    joined_str = re.sub('('+'|'.join('\\b'+re.escape(g)+'\\b' for g in clean_pairs)+')',
                        lambda m: m.group(0).replace(' ', '_'), source)
    pairs_joined.append(joined_str)
    tokens = nltk.word_tokenize(str(pairs_joined))
    token_lower = [str.lower(i) for i in tokens]
    clean_tokens = [i for i in token_lower if i in standard_elements]
    clean_src = clean_tokens + clean_pairs
    return clean_src


def get_number_of_extracted_ingredients(extracted_ingredients):
    missing_ingredients = 0

    for ingredient in extracted_ingredients:
        if ingredient["Ingrediente"] == "None":
            missing_ingredients += 1

    total, extracted, rate = len(extracted_ingredients), (len(
        extracted_ingredients) - missing_ingredients), (len(extracted_ingredients) - missing_ingredients)/len(extracted_ingredients)

    return total, extracted, rate


def extract_quantity(ingredient):
    mixed_unicode_fractions_conversions = {
        '1⅓': 4/3, '1½': 1.5, '2½': 2.5, '3½': 3.5, '4½': 4.5, '5½': 5.5, '6½': 6.5}
    unicode_fraction_conversions = {'¼': 1/4, '2⅓': 2.333, '3⅓': 10/3,
                                    '½': .5, '¾': 3/4, '⅐': 1/7, '⅑': 1/9, '⅒': .1, '⅓': 1/3, '⅔': 2/3, '⅕': .2, '⅖': .4}

    unicode_fractions = list(unicode_fraction_conversions.keys())

    for fraction in mixed_unicode_fractions_conversions:
        if fraction in ingredient:
            return mixed_unicode_fractions_conversions.get(fraction)

    if len(re.findall(r"[-+]?\d*/\d+", ingredient)) != 0:
        return eval((re.findall(r"[-+]?\d*/\d+", ingredient)[0]).replace('⁄', '/').replace('⅟', '1/'))

    if len(re.findall(r"[-+]?\d*\.\d+|\d+", ingredient)) != 0:
        return re.findall(r"[-+]?\d*\.\d+|\d+", ingredient)[0]

    for fraction in unicode_fractions:
        if fraction in ingredient:
            return unicode_fraction_conversions.get(fraction)

    return re.findall(r"[-+]?\d*\.\d+|\d+", ingredient)


def extract_measurement_unit(ingredient):
    # list of measurement units for parsing ingredient
    measurement_units = ['kg', 'kilos',    'kilogramo',    'kilogramos',    'kilo', 'kgr', 'g', 'gr', 'grs', 'cucharillas', 'tarro', 'cucharaditas', 'cucharadas', 'cucharadas soperas', 'cucharadas de postre', 'cucharadas de postre', 'tazas', 'vasos', 'cuencos', 'envases', 'paquetes', 'bolsas', 'latas', 'botellas',
                         'litros', 'paquetes', 'frascos', 'gotas', 'cabezas', 'pellizcos', 'sobres', 'dientes', 'puñados', 'barras', 'cajas', 'copas', 'pizcas', 'chorros', 'chorritos', 'unidades', 'unidad', 'racimos',
                         'lonchas', 'recetas', 'capas', 'rebanadas', 'gajos', 'tallos', 'cuadrados', 'ramas', 'ramitas', 'filetes', 'trozos', 'patas', 'muslos', 'cubos', 'tiras', 'bandejas', 'láminas', 'hojas', 'mitad',
                         'gramos', 'mililitros', 'cucharilla', 'cucharadita', 'cucharada', 'cucharada sopera', 'taza', 'vaso', 'cuenco', 'envase', 'paquete', 'bolsa', 'lata', 'botella', 'litro', 'paquete',
                         'frasco', 'gota', 'cabeza', 'pellizco', 'sobre', 'diente', 'puñado', 'barra', 'caja', 'copa', 'pizca', 'chorro', 'chorrito', 'unidad', 'racimo', 'loncha', 'receta',
                         'capa', 'rebanada', 'gajo', 'tallo', 'cuadrado', 'pechuga', 'rama', 'ramita', 'filete', 'trozo', 'pata', 'muslo', 'cubo', 'tira', 'bandeja', 'lámina', 'hoja', 'gramo', 'mililitro', 'al gusto']

    extracted_1_grams = extract_n_grams(ingredient, 1, measurement_units)
    extracted_2_grams = extract_n_grams(ingredient, 2, measurement_units)
    extracted_3_grams = extract_n_grams(ingredient, 3, measurement_units)

    extracted_measurement_unit_raw = extracted_1_grams + \
        extracted_2_grams + extracted_3_grams
    extracted_measurement_unit = list(
        dict.fromkeys(extracted_measurement_unit_raw))

    if len(extracted_measurement_unit) == 0:
        return "None"
    elif len(extracted_measurement_unit) == 1:
        return extracted_measurement_unit[0]
    elif len(extracted_measurement_unit) > 1:
        for item in extracted_measurement_unit:
            if item in ['g', 'gr', 'grs','gramos','gramo']: #comprobar si alguna de las coincidencias parseadas es gramos, si lo es la devuelve
                return item 
        return max(extracted_measurement_unit, key=len) #si ninguna es, devuelve la más larga



def extract_ingredient(ingredient, bedca_ingredients):
    extracted_1_grams = extract_n_grams(ingredient, 1, bedca_ingredients)
    extracted_2_grams = extract_n_grams(ingredient, 2, bedca_ingredients)
    # TODO : Documentar por qué no llega solo con 3-gramas
    extracted_3_grams = extract_n_grams(ingredient, 3, bedca_ingredients)

    extracted_ingredient_raw = extracted_1_grams + \
        extracted_2_grams + extracted_3_grams
    extracted_ingredient = list(dict.fromkeys(extracted_ingredient_raw))

    if len(extracted_ingredient) == 0:
        return "None"
    elif len(extracted_ingredient) == 1:
        return extracted_ingredient[0]
    elif len(extracted_ingredient) > 1:
        # when it finds 2 matches for the same string (keep the longer one)
        return max(extracted_ingredient, key=len)


def parse_ingredient_string(ingredients_string, bedca_ingredients, log_console=False):
    # TO DO: añadir soporte para ingredientes de la forma (1 limón) (sin unidades de medida) --> Sería comprobar si no existen unidades de medida entre las soportadas
    ingredient_list = ingredients_string.split(',')

    parsed_ingredients = []

    for ingredient in ingredient_list:
        extracted_ingredient = {}

        extracted_ingredient["Ingrediente"] = extract_ingredient(
            ingredient, bedca_ingredients)
        extracted_ingredient["Cantidad"] = extract_quantity(ingredient)
        extracted_ingredient["Unidad"] = extract_measurement_unit(ingredient)


        parsed_ingredients.append(extracted_ingredient)

    total, extracted, rate = get_number_of_extracted_ingredients(
        parsed_ingredients)

    if log_console == True:
        print("TOTAL: ", total)
        print("EXTRACTED: ", extracted)
        print("RATE: ", rate)

    return parsed_ingredients, rate, total, extracted


def measure_average_rate(recipes, log_to_csv=False):  # TODO: reformatear
    '''

    Itera todo el dataset de recetas extrayendo los ingredientes y calculando el
    ratio de extracción, el número total de ingredientes y el total de ingredientes
    extraídos.

    Retorna el promedio de extracción

    '''
    rates = []
    error_index = []

    recipes_ingredients = recipes[["Id", "Ingredientes"]].copy()

    ingredients = pd.read_csv('../../data/bedca.csv')
    ingredients_names = ingredients["nombre"].tolist()

    all_ingredients = ingredients_to_plural(
        ingredients_names)  # ingredientes originales + plurales
    bedca_ingredients = [x.lower() for x in all_ingredients]

    print("recipes size: ", recipes_ingredients.shape[0])

    for index, value in recipes_ingredients.iterrows():
        print("current/recipes size: ", index,
              "/", recipes_ingredients.shape[0])
        try:
            clean_ingr, rate, total, extracted = parse_ingredient_string(
                value["Ingredientes"], bedca_ingredients)
            rates.append(rate)
            recipes.loc[index, 'parse_rate'] = rate
            recipes.loc[index, 'total_ingredients'] = total
            recipes.loc[index, 'parsed_ingredients'] = extracted
        except:
            print("Error in recipe ", index)
            error_index.append(index)
            rates.append(0)
            recipes.loc[index, 'parse_rate'] = 0
            recipes.loc[index, 'total_ingredients'] = 0
            recipes.loc[index, 'parsed_ingredients'] = 0

    print("AVERAGE PERCENT OF INGREDIENTS EXTRACTED= ", sum(rates)/len(rates))
    print("Errors in recipes: ", error_index)
    if log_to_csv == True:
        recipes.to_csv('../../data/output_with_rates.csv',
                       index=False, header=True, sep='|')

    return


def filter_dataset():
    '''Filters the dataset to keep recipes with parse rate > 85%'''
    recipes = pd.read_csv('../../data/output_with_rates.csv', sep='|')
    recipes_filtered = recipes[recipes['parse_rate'] >= 0.85]
    recipes_filtered.to_csv('../../data/filtered_recipes.csv',
                            index=False, header=True, sep='|')

    return


def filter_dataset_100():
    '''Filters the dataset to keep recipes with parse rate > 85%'''
    recipes = pd.read_csv('../../data/output_with_rates.csv', sep='|')
    recipes_filtered = recipes[recipes['parse_rate'] == 1.0]
    recipes_filtered.to_csv(
        '../../data/filtered_recipes_100.csv', index=False, header=True, sep='|')

    return


def extraction_analysis():
    recipes = pd.read_csv('../../data/output_with_rates.csv', sep='|')

    print("# of recipes with 100% extracted rate:",
          len(recipes[(recipes['parse_rate'] == 1.0)]))
    print("# of recipes with >90% and <100% extracted rate:", len(
        recipes[(recipes['parse_rate'] >= 0.90) & (recipes['parse_rate'] < 1.0)]))
    print("# of recipes with >85% and <90% extracted rate:", len(
        recipes[(recipes['parse_rate'] >= 0.8) & (recipes['parse_rate'] < 0.90)]))
    print("# of recipes missing only 1 ingredient: ", len(
        recipes[(recipes['total_ingredients'] - recipes['parsed_ingredients'] <= 1)]))

    return


def add_recipe_ingredients_to_df(df, clean_ingr, recipe_id, bedca_ingredients, bedca_ingredients_lower_plurals_dict):
    '''Adds the extracted ingredients to the recipe ingredients DataFrame'''

    for index in range(len(clean_ingr)):

        if clean_ingr[index]["Ingrediente"] in list(bedca_ingredients_lower_plurals_dict.keys()):
            ingredient_name = clean_ingr[index]["Ingrediente"]
        elif clean_ingr[index]["Ingrediente"] in list(bedca_ingredients_lower_plurals_dict.values()):
            # in python 3, you'll need `list(i.keys())`
            keys = list(bedca_ingredients_lower_plurals_dict.keys())
            values = list(bedca_ingredients_lower_plurals_dict.values())
            ingredient_name = keys[values.index(
                clean_ingr[index]["Ingrediente"])]

        recipe_id = int(recipe_id)

        if clean_ingr[index]["Cantidad"] == []:
            ingredient_quantity = np.nan
        else:
            ingredient_quantity = clean_ingr[index]["Cantidad"]

        if clean_ingr[index]["Unidad"] == []:
            ingredient_unit = np.nan
            grams_equivalence = np.nan
        else:
            ingredient_unit = clean_ingr[index]["Unidad"]
            grams_equivalence = equivalences.get(
                clean_ingr[index]["Unidad"], np.nan)

        bedca_index = int(bedca_ingredients.index(ingredient_name))

        grams_equivalence = equivalences.get(
            clean_ingr[index]["Unidad"], np.nan)

        total_grams = float(ingredient_quantity) * grams_equivalence

        df = df.append(pd.Series([recipe_id, ingredient_name, ingredient_quantity, ingredient_unit,
                                  bedca_index,
                                  grams_equivalence,
                                  total_grams],
                                 index=['Recipe_id', 'Ingrediente', 'Cantidad', 'Unidad', 'Indice', 'Grams', 'Total_Grams']), ignore_index=True)

    return df


def extract_ingredients_to_csv(recipes):  # TODO: reformatear

    recipes_ingredients_df = pd.DataFrame(
        columns=['Recipe_id', 'Ingrediente', 'Cantidad', 'Unidad', 'Indice', 'Grams', 'Total_Grams'])
    #recipe_ingredients_df=pd.read_csv('../../data/ingredientes.csv', sep='|',names=['Recipe_id', 'Ingrediente', 'Cantidad','Unidad','Indice','Grams','Total_Grams'])

    recipes_ingredients = recipes[["Id", "Ingredientes"]].copy()

    ingredients = pd.read_csv('../../data/bedca.csv')
    bedca_ingredients = ingredients["nombre"].tolist()
    bedca_ingredients_lower = [x.lower() for x in bedca_ingredients]

    bedca_ingredients_lower_with_plurals = ingredients_to_plural(
        bedca_ingredients_lower)  # ingredientes originales + plurales

    bedca_ingredients_lower_plurals_dict = ingredients_to_plural_dict(
        bedca_ingredients_lower)

    print("recipes size: ", recipes_ingredients.shape[0])

    for index, value in recipes_ingredients.iterrows():
        print("current/recipes size: ", index,
              "/", recipes_ingredients.shape[0])
        clean_ingr, rate, total, extracted = parse_ingredient_string(
            value["Ingredientes"], bedca_ingredients_lower_with_plurals)
        recipes_ingredients_df = add_recipe_ingredients_to_df(
            recipes_ingredients_df, clean_ingr, value["Id"], bedca_ingredients_lower, bedca_ingredients_lower_plurals_dict)

    recipes_ingredients_df.to_csv(
        '../../data/ingredientes.csv', index=False, header=True, sep=',')

    return


def main():
    #recipes = pd.read_csv('../../data/output.csv', sep='|')
    recipes = pd.read_csv('../../data/filtered_recipes_100.csv', sep='|')
    recipes = recipes[recipes['Ingredientes'].notna()]
    # print(recipes["parse_rate"].mean())
    recipes_ingredients = recipes[["Id", "Ingredientes"]].copy()

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
    # TODO 45 -> pilla nuez y nuez moscada, arreglar alubias y frijoles
    # TODO -> Añadir soporte para las tildes

    test_ingredients = recipes_ingredients.iloc[1021, :]
    ingredients_id = test_ingredients["Id"]
    # Recetas para testing -> [74146, 73727, 74020 , 73919, 73818, 73799,73756, 73360, 73314, 73269, 72692, 72311, 72126,66092, 65997, 71629]
    ingredients_string = test_ingredients["Ingredientes"]
    print("RAW INGREDIENT STRING for recipe",
          ingredients_id,  ":",  ingredients_string)

    recipe_ingredients_df = pd.read_csv('../../data/ingredientes.csv', sep='|', names=[
                                        'Recipe_id', 'Ingrediente', 'Cantidad', 'Unidad', 'Indice', 'Grams', 'Total_Grams'])

    clean_ingr, rate, total, extracted = parse_ingredient_string(
        ingredients_string, bedca_ingredients_lower_with_plurals, log_console=True)
    # add_recipe_ingredients_to_df(recipe_ingredients_df,clean_ingr,ingredients_id,bedca_ingredients_lower,bedca_ingredients_lower_plurals_dict)
    print("EXTRACTED_INGREDIENTS: ", clean_ingr)

    #measure_average_rate(recipes, bedca_ingredients,ingredients_id,bedca_ingredients_lower)

    # extraction_analysis()
    extract_ingredients_to_csv(recipes)
    # filter_dataset_100()

    return


if __name__ == "__main__":
    main()
