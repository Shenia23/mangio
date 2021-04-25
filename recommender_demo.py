from app.recommender.recommender import *

preferences = {'Carne': 1.05, 
'Pollo': 0.3333333333333333, 
'Pescado': 0.3666666666666667, 
'Legumbres': 0.8833333333333334, 
'Verduras': -0.4, 'Patatas': 0.275, 'Arroz': 0.0, 'Pasta': 0.25, 
'Huevos': -0.5833333333333333}

recommender = Recommender(2000, 2, preferences)
start = time.time()
recommendation = recommender.recommend()
end = time.time()
print("Recommendation time: ", end-start)
print(recommendation[['Recipe_id','Comida','Total_Grams','Nombre','energia','proteina','grasa','carbohidratos']])

recommendation['pref_score'] = recommendation['Recipe_id'].apply(Recommender.get_preferences_score, preferences = preferences)
print(recommendation[['Nombre','pref_score']])