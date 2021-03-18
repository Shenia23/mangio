import pandas as pd
import pattern.es as es

'''
Código para cambiar palabras en el CSV de recetas, se introducen las equivalencias
que deben ser cambiadas en la lista.

'''
input_path = '../../data/recetas.csv'
output_path = '../../data/output.csv'

#esto podría ir en un json aparte
words = {
    "jitomate": "tomate",
    "papa": "patata",
    "jugo": "zumo",
    "res": "vaca",
    "catsup": "ketchup",
    "olivas": "aceitunas",
    "maní": "cacahuete",
    "banana": "plátano",
    "toronja": "pomelo",
    "habichuela": "alubia",
    "frijol": "alubia",
    "alcaucil": "alcachofa",
    "poroto": "alubia",
    "batata": "boniato",
    "camote": "boniato",
    "chicharo": "garbanzo",
    "salame": "salchichón",
    "salsa blanca": "salsa bechamel",
    "jamón de pavo":"pavo",
    "guinda": "cereza",
    "durazno": "melocotón",
    "arveja": "guisante",
    "ejote": "judía verde",
    "cohombro": "pepino",
    "bife": "bacon",
    "paprika":"pimentón",
    "chalota" : "cebolla",
    "echalote" : "cebolla",
    "chalote" : "cebolla",
    "cilantro" : "perejil",
    "coca-cola" : "refresco de cola",
    "jamón york":"jamón de york",
    "soya":"soja",
    "mahonesa":"mayonesa",
    "callampo": "champiñón",
    "chancho": "cerdo",
    "puerco": "cerdo",
    "pan molido": "pan rallado",
    "hierbabuena":"menta"
}


def ingredients_to_plural(ingredients):
    '''
    Add Pluralized bbc ingredients in order to catch ingredients like tomatoes, carrots, etc
    '''
    all_ingredients = dict()
    for key,value in ingredients.items():
        all_ingredients[es.pluralize(key)] = es.pluralize(value)
        all_ingredients[key.capitalize()] = value.capitalize()
    ingredients.update(all_ingredients)
    return ingredients

def regex_keys(ingredients):
    '''
    Add regex rules to keys to avoid replacing similar words accidentaly ej. jugoso -> zumoso
    '''
    regex_dict = dict()
    for key,value in ingredients.items():
        regex_dict['\\b'+key+'\\b'] = value
    return regex_dict

def normalize_df(df):
    '''
    Lowercase ingredients, capitalized titles
    '''
    df['Ingredientes'] = df['Ingredientes'].str.lower()
    df['Nombre'] = df['Nombre'].str.lower()
    df['Nombre'] = df['Nombre'].str.capitalize()
    return df

def replace_ingredients(df,words_to_replace):
    '''
    Replaces uncommon words in a given df (Ingredientes and Nombre columns only)
    '''
    replacements = ingredients_to_plural(words_to_replace)
    print('Replacing the following words: ', replacements)
    df = normalize_df(df)
    df['Nombre'] = df['Nombre'].replace(regex_keys(replacements), regex=True)
    df['Ingredientes'] = df['Ingredientes'].replace(regex_keys(replacements), regex=True)
    return df

if __name__ == "__main__":
    df = pd.read_csv(input_path,sep='|')
    standarized_df = replace_ingredients(df,words)
    standarized_df.to_csv(output_path,sep='|',index=False)