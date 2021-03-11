from functools import reduce

import pandas as pd
import csv
import re

'''
Código para cambiar palabras en el CSV de recetas, se introducen las equivalencias
que deben ser cambiadas en la lista.

'''

# Para no cambiar las palabras en las URLs
def manageCol():
    df = pd.read_csv('../../data/recetas.csv',sep='|')
    urls = df['Link_receta']
    del df['Link_receta']
    df.to_csv('../../data/output.csv',sep='|',index=False)
    return urls

def saveCSV(text,urls):
    x = open("../../data/output.csv", "w", encoding="utf8")
    x.writelines(text)
    x.close()
    df = pd.read_csv('../../data/output.csv',sep='|')
    df['Link_receta'] = urls
    df.to_csv('../../data/output.csv',sep='|',index=False)

#Llamar para observar si alguna se quedo igual, fuera de los links
def viewer():
    df = pd.read_csv('../../data/output.csv',sep='|')
    del df['Link_receta']
    df.to_csv('../../data/output.csv',sep='|')

def change_words(word1,word2,text):
    text = ''.join([i for i in text]).replace(' '+word1,' '+word2)
    text = ''.join([i for i in text]).replace(word1+' ',' '+word2+' ')
    text = ''.join([i for i in text]).replace(','+word1,','+word2)
    text = ''.join([i for i in text]).replace('('+word1,'('+word2)
    text = ''.join([i for i in text]).replace(word1+',',word2+',')
    text = ''.join([i for i in text]).replace(word1+'.',word2+'.')
    text = ''.join([i for i in text]).replace(word1.capitalize(),word2.capitalize())
    text = ''.join([i for i in text]).replace(word1.upper(),word2.upper())
    return text



urls = manageCol()
text = open("../../data/output.csv", "r", encoding="utf8")

words = [
    ("papa", "patata"),
    ("jitomate", "tomate"),
    ("jugo", "zumo")
]





for pair in words:
    text = change_words(pair[0], pair[1],text)

saveCSV(text,urls)

viewer()
