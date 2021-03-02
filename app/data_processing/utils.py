import pandas as pd
import pattern.es as es
from nltk.stem import PorterStemmer
import nltk
from nltk.stem import WordNetLemmatizer
import re

recipes = pd.read_csv('../../data/recetas.csv', sep='|')
ingredients = pd.read_csv('../../data/bedca.csv')


ingredients_names = ingredients["nombre"].tolist()


test1 = recipes["Ingredientes"].loc[2500].split(",")
print("Ingredients Test String: ",test1)

def ingredients_to_plural(ingredients_raw):
    #Add Pluralized bbc ingredients in order to catch ingredients like tomatoes, carrots, etc
    ingredients_plural = []
    for i in ingredients_raw: 
        if len(i.split(' ')) == 1:
            ingredients_plural.append(es.pluralize(i))#añadimos a la lista los plurales de aquellos que sean una sola palabra
    ingredients_raw = ingredients_raw + ingredients_plural
    return ingredients_raw


all_ingredients = ingredients_to_plural(ingredients_names) #ingredientes originales + plurales
all_ingredients_lower = [x.lower() for x in all_ingredients]

ps = PorterStemmer()

def clean_ingredients(ingredients):
    extracted_1_grams = extract_n_grams(ingredients, 1)
    extracted_2_grams = extract_n_grams(ingredients, 2)
    extracted_3_grams = extract_n_grams(ingredients, 3)
    extracted_ingredients_raw = extracted_1_grams + extracted_2_grams +extracted_3_grams # 
    extracted_ingredients = list(dict.fromkeys(extracted_ingredients_raw))
    return extracted_ingredients

def extract_n_grams(ingredients, n_grams):
    
    ingr = [x for x in ingredients]
    tokens = nltk.word_tokenize(str(ingr))
    token_lower = [str.lower(i) for i in tokens]
    print("token_lower:", token_lower)
    pairs = [" ".join(pair).replace("'","") for pair in nltk.ngrams(token_lower, n_grams)]
    #print("pairs: ",pairs)
    clean_pairs = [i for i in pairs if i in all_ingredients_lower]
    pairs_joined = []
    for i in ingr:
        joined_str = re.sub('('+'|'.join('\\b'+re.escape(g)+'\\b' for g in clean_pairs)+')',lambda m: m.group(0).replace(' ', '_'),i)
        pairs_joined.append(joined_str)
    tokens = nltk.word_tokenize(str(pairs_joined))
    token_lower = [str.lower(i) for i in tokens]
    clean_tokens = [i for i in token_lower if i in all_ingredients_lower] 
    clean_ingr = clean_tokens + clean_pairs
    return clean_ingr
    

clean_ingr= clean_ingredients(test1)

print("Extracted ingredients: ", clean_ingr)

print("Original_ingr_size: ", len(test1))
print("Clean_ingr_size: ", len(clean_ingr))