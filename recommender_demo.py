from app.recommender.recommender import *

recommender = Recommender(2500, 1)
recommendation = recommender.recommend()
print(recommender.get_macros_in_grams())
print(recommendation[['Comida','Total_Grams','Nombre','energia','proteina','grasa','carbohidratos']])