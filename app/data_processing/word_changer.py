from functools import reduce

import pandas as pd
import pattern.es as es

'''
Código para cambiar palabras en el CSV de recetas, se introducen las equivalencias
que deben ser cambiadas en la lista.

'''
input_path = '../../data/recetas.csv'
output_path = '../../data/output.csv'
words = [
    #("papa", "patata"),
    # ("jitomate", "tomate"),
     ("jugo", "zumo")
]

#buscar también plurales
def ingredients_to_plural(ingredients_raw):
    # Add Pluralized bbc ingredients in order to catch ingredients like tomatoes, carrots, etc
    ingredients_plural = []
    for pair in words:
        tuple = (es.pluralize(pair[0]),es.pluralize(pair[1]))
        ingredients_plural.append(tuple)
    ingredients_raw = ingredients_raw + ingredients_plural
    return ingredients_raw

def change_words(word1,word2,text):
    text = ''.join([i for i in text]).replace(' '+word1+' ',' '+word2+' ')
    text = ''.join([i for i in text]).replace(','+word1+' ',','+word2+' ')
    text = ''.join([i for i in text]).replace(' '+word1+',',' '+word2+',')
    text = ''.join([i for i in text]).replace(','+word1+',',','+word2+',')
    text = ''.join([i for i in text]).replace(' ' + word1 + '.', ' ' + word2 + '.')
    text = ''.join([i for i in text]).replace('.' + word1 + ' ', '.' + word2 + ' ')
    text = ''.join([i for i in text]).replace(' '+word1+'|',' '+word2+'|')
    text = ''.join([i for i in text]).replace('|'+word1+',','|'+word2+',')
    text = ''.join([i for i in text]).replace('|'+word1+' ','|'+word2+' ')
    text = ''.join([i for i in text]).replace('('+word1,'('+word2)
    text = ''.join([i for i in text]).replace(' ' + word1 + '(', ' ' + word2 + '(')
    text = ''.join([i for i in text]).replace(' ' + word1 + ')', ' ' + word2 + ')')
    text = ''.join([i for i in text]).replace(',' + word1 + ')', ',' + word2 + ')')
    text = ''.join([i for i in text]).replace(',' + word1 + '(', ',' + word2 + '(')
    text = ''.join([i for i in text]).replace(' ' + word1 + '\n', ' ' + word2 + '\n')
    text = ''.join([i for i in text]).replace(',' + word1 + '\n', ',' + word2 + '\n')
    return text

# Para no cambiar las palabras en las URLs
def manageCol():
    df = pd.read_csv(input_path,sep='|')
    urls = df['Link_receta']
    del df['Link_receta']
    df.to_csv(output_path,sep='|',index=False)
    return urls

def saveCSV(text,urls):
    x = open(output_path, "w", encoding="utf8")
    x.writelines(text)
    x.close()
    df = pd.read_csv(output_path,sep='|')
    df['Link_receta'] = urls
    df.to_csv(output_path,sep='|',index=False)

#Llamar para observar si alguna se quedo igual, fuera de los links
def viewer():
    df = pd.read_csv(output_path,sep='|')
    del df['Link_receta']
    df.to_csv(output_path,sep='|')


def main():
    urls = manageCol()
    text = open(output_path, "r", encoding="utf8")
    all_words = ingredients_to_plural(words)

    for pair in all_words:
        text = change_words(pair[0], pair[1],text)
        text = change_words(pair[0].capitalize(), pair[1].capitalize(),text)
        text = change_words(pair[0].upper(), pair[1].upper(),text)


    saveCSV(text,urls)
    #viewer()

if __name__ == "__main__":
    main()
