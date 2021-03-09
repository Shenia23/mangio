import re
import unicodedata


'''
Procedimiento para extracción de valores numéricos:
1. Comprobar si hay fracciones unicode
2. Si no hay fracciones unicode comprobar si hay fracciones con '/'
3. Si no comprobar si hay enteros o floats (con '.')
4. Devolver el valor obtenido


'''
def parse_quantity(ingredient):
   
   unicode_fraction_conversions = {'1⅓':4/3,'1½':1.5,'2½':2.5,'3½':3.5,'4½':4.5,'5½':5.5,'6½':6.5,'¼': 1/4, '2⅓':2.333,'3⅓':10/3,
           '½': .5, '¾': 3/4, '⅐': 1/7, '⅑': 1/9, '⅒': .1, '⅓': 1/3, '⅔': 2/3, '⅕': .2, '⅖': .4}
   
   unicode_fractions=list(unicode_fraction_conversions.keys())
   
   for fraction in unicode_fractions:
       if fraction in ingredient:
           return unicode_fraction_conversions.get(fraction) 

   if len(re.findall(r"[-+]?\d*/\d+", ingredient)) !=0: 
       return eval((re.findall(r"[-+]?\d*/\d+", ingredient)[0]).replace('⁄', '/').replace('⅟', '1/'))
   
   return re.findall(r"[-+]?\d*\.\d+|\d+", ingredient)





ingredient = "2/3ml caldo pollo"


print(parse_quantity(ingredient))





