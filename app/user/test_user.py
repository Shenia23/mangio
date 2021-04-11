from user import User, createNewUser
import json

userData = {'username': 'giulia_50',
            'name': 'Giulia',  
            'age': 65,
            'sex': 'Mujer',
            'weight': 70,
            'height': 170,
            'body_type': 'Endomorfo',
            'activity_level': 1,
            'objective': 1,
            'liked_ingredients': None,
            'using_scale' : False
            }

new_user = createNewUser(userData)

print(new_user)

with open("./users/giulia_50_data.json","r") as json_file:
    data = json.load(json_file)

    print ("Existing:", type(data))
    new_user_2 = createNewUser(data)

    print(new_user_2)