from app.recommender.recommender import *
from app.recommender.recom_constants import *

preferences = {'Carne': 1.05, 
'Pollo': 0.3333333333333333, 
'Pescado': 0.3666666666666667, 
'Legumbres': 0.8833333333333334, 
'Verduras': -0.4, 'Patatas': 0.275, 'Arroz': 0.0, 'Pasta': 0.25, 
'Huevos': -0.5833333333333333}

columns = ['Recipe_id','Comida','Total_Grams','Nombre','energia','proteina','grasa','carbohidratos','preference_score']

recommender = Recommender(2000, 2, preferences, 0.7)
start = time.time()
recommendation = recommender.recommend()
end = time.time()
print("Recommendation time: ", end-start)
print(recommendation[columns])


reroll_id = recommendation.reset_index().loc[4, ['Recipe_id']].values
most_similar = recommender.most_similar(reroll_id[0],'comida')
print(most_similar[columns])

print(recipes2dict(most_similar))

