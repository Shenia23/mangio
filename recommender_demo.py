from app.recommender.recommender import *

recommender = Recommender(2500, 1)
recommendation = recommender.recommend()
print(recommendation[['Comida','Total_Grams','Nombre','energia','proteina','grasa','carbohidratos']])