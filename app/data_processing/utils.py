import pandas as pd
import pattern.es as es
import nltk
from nltk.stem import WordNetLemmatizer
import re





def ingredients_to_plural(ingredients_raw):
    #Add Pluralized bbc ingredients in order to catch ingredients like tomatoes, carrots, etc
    ingredients_plural = []
    for i in ingredients_raw: 
        if len(i.split(' ')) == 1:
            ingredients_plural.append(es.pluralize(i))#añadimos a la lista los plurales de aquellos que sean una sola palabra
    ingredients_raw = ingredients_raw + ingredients_plural
    return ingredients_raw





def extract_n_grams(source, n_grams, standard_elements):

    tokens = nltk.word_tokenize(str(source))
    token_lower = [str.lower(i) for i in tokens]
    pairs = [" ".join(pair).replace("'","") for pair in nltk.ngrams(token_lower, n_grams)]
    clean_pairs = [i for i in pairs if i in standard_elements]
    pairs_joined = []
    joined_str = re.sub('('+'|'.join('\\b'+re.escape(g)+'\\b' for g in clean_pairs)+')',lambda m: m.group(0).replace(' ', '_'),source)
    pairs_joined.append(joined_str)
    tokens = nltk.word_tokenize(str(pairs_joined))
    token_lower = [str.lower(i) for i in tokens]
    clean_tokens = [i for i in token_lower if i in standard_elements] 
    clean_src = clean_tokens + clean_pairs
    return clean_src 

def get_number_of_extracted_ingredients(extracted_ingredients):
    missing_ingredients = 0
    
    for ingredient in extracted_ingredients:
        if ingredient["Ingrediente"] == "unavailable ingredient":
            missing_ingredients+=1
        
    total, extracted, rate = len(extracted_ingredients), (len(extracted_ingredients) - missing_ingredients), (len(extracted_ingredients) - missing_ingredients)/len(extracted_ingredients)
    
    return total, extracted, rate

def measure_average_rate(recipes_ingredients): # TODO: reformatear
    find_rates = []

    for index, value in recipes_ingredients.iteritems():
        #print(index/recipes.shape[0])
        clean_ingr, rate = clean_ingredients(value.split(","))
        find_rates.append(rate)
        
    print("AVERAGE PERCENT OF INGREDIENTS EXTRACTED: ", sum(find_rates)/len(find_rates))

def extract_quantity(ingredient):  
    return 0

def extract_measurement_unit(ingredient):
    # list of measurement units for parsing ingredient
    measurement_units = ['cucharillas', 'cucharaditas', 'cucharadas', 'cucharadas soperas', 'cucharadas de postre','cucharadas de postre', 'tazas', 'vasos', 'cuencos', 'envases', 'paquetes', 'bolsas', 'latas', 'botellas', 
                    'litros', 'paquetes', 'frascos', 'gotas', 'cabezas', 'pellizcos', 'sobres', 'dientes', 'puñados', 'barras', 'cajas', 'copas', 'pizcas', 'chorros', 'chorritos', 'unidades', 'unidad', 'racimos', 
                    'lonchas', 'recetas', 'capas', 'rebanadas', 'gajos', 'tallos', 'cuadrados', 'ramas', 'ramitas', 'filetes', 'trozos', 'patas', 'muslos', 'cubos', 'tiras', 'bandejas', 'láminas', 'hojas', 'mitad', 
                    'gramos', 'mililitros', 'cucharilla', 'cucharadita', 'cucharada', 'cucharada sopera', 'taza', 'vaso', 'cuenco', 'envase', 'paquete', 'bolsa', 'lata', 'botella', 'litro', 'paquete', 
                    'frasco', 'gota', 'cabeza', 'pellizco', 'sobre', 'diente', 'puñado', 'barra', 'caja', 'copa', 'pizca', 'chorro', 'chorrito', 'unidad', 'racimo', 'loncha', 'receta', 
                    'capa', 'rebanada', 'gajo', 'tallo', 'cuadrado', 'rama', 'ramita', 'filete', 'trozo', 'pata', 'muslo', 'cubo', 'tira', 'bandeja', 'lámina', 'hoja', 'gramo', 'mililitro']
    
    extracted_1_grams = extract_n_grams(ingredient, 1, measurement_units)
    extracted_2_grams = extract_n_grams(ingredient, 2, measurement_units)
    extracted_3_grams = extract_n_grams(ingredient, 3, measurement_units)
    
    extracted_measurement_unit_raw = extracted_1_grams + extracted_2_grams +extracted_3_grams# 
    extracted_measurement_unit = list(dict.fromkeys(extracted_measurement_unit_raw))
    
    if len(extracted_measurement_unit) == 0:
        return "unavailable measurement unit"
    elif len(extracted_measurement_unit) == 1:
        return extracted_measurement_unit 
    elif len(extracted_measurement_unit) > 1:
        return max(extracted_measurement_unit, key=len) #when it finds 2 matches for the same string (keep the longer one)
  

def extract_ingredient(ingredient, bedca_ingredients):
    extracted_1_grams = extract_n_grams(ingredient, 1,bedca_ingredients)
    extracted_2_grams = extract_n_grams(ingredient, 2,bedca_ingredients)
    extracted_3_grams = extract_n_grams(ingredient, 3,bedca_ingredients) #TODO : Documentar por qué no llega solo con 3-gramas

    extracted_ingredient_raw = extracted_1_grams + extracted_2_grams +extracted_3_grams# 
    extracted_ingredient = list(dict.fromkeys(extracted_ingredient_raw))
    
    if len(extracted_ingredient) == 0:
        return "unavailable ingredient"
    elif len(extracted_ingredient) == 1:
        return extracted_ingredient 
    elif len(extracted_ingredient) > 1:
        return max(extracted_ingredient, key=len) #when it finds 2 matches for the same string (keep the longer one)

    
def parse_ingredient_string(ingredients_string, bedca_ingredients):
    ingredient_list = ingredients_string.split(',')
    
    
    parsed_ingredients = []
    
    for ingredient in ingredient_list:
        extracted_ingredient={}
        
        extracted_ingredient["Ingrediente"] = extract_ingredient(ingredient,bedca_ingredients)
        extracted_ingredient["Cantidad"] = extract_quantity(ingredient)
        extracted_ingredient["Unidad"] = extract_measurement_unit(ingredient)
        
        parsed_ingredients.append(extracted_ingredient)
    
    total, extracted , rate = get_number_of_extracted_ingredients(parsed_ingredients)
    print("TOTAL: ",total)
    print("EXTRACTED: ", extracted)
    print("RATE: ",rate)
    
    return parsed_ingredients 


    
def main():
    recipes = pd.read_csv('../../data/recetas.csv', sep='|')
    recipes_ingredients = recipes["Ingredientes"]
    recipes_ingredients.dropna(inplace=True)

    ingredients = pd.read_csv('../../data/bedca.csv')
    ingredients_names = ingredients["nombre"].tolist()

    all_ingredients = ingredients_to_plural(ingredients_names) #ingredientes originales + plurales
    bedca_ingredients = [x.lower() for x in all_ingredients]
    recipes.reset_index(drop=True, inplace = True)
    print("NUM_RECETAS: ",recipes_ingredients.shape[0])
    
    # TODO 45 -> pilla nuez y nuez moscada, arreglar alubias y frijoles
    ingredients_string = recipes_ingredients.loc[1020]
    print("RAW INGREDIENT STRING: ",ingredients_string)

        
        
    #clean_ingr, rate=clean_ingredients(ingredient_list)
    print("EXTRACTED_INGREDIENTS: ", parse_ingredient_string(ingredients_string, bedca_ingredients))


   # measure_average_rate(recipes_ingredients)

if __name__ == "__main__":
    main()  

