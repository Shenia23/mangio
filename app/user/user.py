import json
import os
from types import SimpleNamespace
import jsonpickle

class User:
    
    '''Esta clase define un perfil de un usuario de nuestro sistema, con todos los datos necesarios para generar recomendaciones.
        Además, almacena los parámetros necesarios para la monitorización de su estado físico a través de la bascula Xiaomi.'''
    
    def __init__(self, username,name, sex, age, height, weight, 
                 body_type, activity_level, liked_ingredients,
                 objective, disliked_ingredients = None,scale_data = None ,using_scale = False, serialize  = False ):
        
        '''Constructor de la clase de usuario, scale_data es un dict con los parámetros de la báscula'''
        self.username = username
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.body_type = body_type # Ectomorfo, mesomorfo, o endomorfo
        self.activity_level= activity_level  # Nivel de actividad física del usuario (de los definidos en el Excel)
        self.liked_ingredients = liked_ingredients
        self.disliked_ingredients = disliked_ingredients
        self.objective = objective # Ganar masa muscular, mantenerse, adelgazar
        self.using_scale = using_scale
        
        if using_scale == False:
            
            self.weight = weight
            self.bmi = self.get_bmi()
            self.bmr = self.get_bmr()
            self.tdee= self.get_tdee()
            self.water_intake = self.get_daily_water_intake()
            
        elif using_scale == True:
            
            self.weight = scale_data["weight"]
            self.bmi = scale_data["bmi"]
            self.lean_body_mass = scale_data["lean_body_mass"]
            self.bmr = scale_data["basal_metabolism"] 
            self.body_fat = scale_data["body_fat"]
            self.visceral_fat = scale_data["visceral_fat"]
            self.muscle_mass = scale_data["muscle_mass"]
            self.body_water = scale_data["water"]
            self.bone_mass = scale_data["bone_mass"]
            self.protein = scale_data["protein"]
            self.body_condition =  scale_data["body_type"]
            self.metabolic_age = scale_data["metabolic_age"]
            self.tdee= self.get_tdee()
            self.water_intake = self.get_daily_water_intake()
        
        if serialize  == True:
            self.user_to_json()

    def user_to_json(self):
        #print("Current path:",os.getcwd())
        #file_name= "./app/user/users/"+self.username+"_data.json"
        file_name= "./app/user/users/"+self.username+"_data.json"
        print("self.dict: ",self.__dict__)
        with open(file_name, 'w') as f:
            json.dump(self.__dict__, f, indent=4, sort_keys=False)
        return
        
    def __str__(self):
        user_str = ""
        user_str += "{ username = "+ self.username +","
        user_str += " name = "+ self.name +","
        user_str += " age = "+ str(self.age) +","
        user_str += " sex = "+ self.sex +","
        user_str += " body_type = "+ self.body_type +","
        user_str += " height = "+ str(self.height) +","
        user_str += " weight = "+ str(self.weight) +","
        user_str += " activity_level = "+ str(self.activity_level) +","
        user_str += " objective = "+ str(self.objective) +","
        user_str += " bmr = "+ str(self.bmr) +","
        user_str += " tdee = "+ str(self.tdee) +","
        user_str += " liked_ingredients = "+ str(self.liked_ingredients) +"}"
        return user_str
        
    def get_bmi(self):
        
        '''Cálculo del BMI (índice de masa corporal) para el caso de no conectar con la báscula'''

        return self.weight / ((self.height / 100) ** 2)
        
    def get_bmr(self):
        
        '''Cálculo del BMR (metabolismo basal) para el caso de no conectar con la báscula'''
        if self.sex == "Hombre":
            return 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
        elif self.sex == "Mujer":
            return 655.1 + (9.563 * self.weight) + (1.85 * self.height) - (4.676 * self.age)
        
    def get_tdee(self):
        
        '''Cálculo del consumo calórico total diario en función del metabolismo basal y del factor de actividad física'''

        factor= { #Factor de ajuste correspondiente al nivel de actividad física
            1: 1.2,   # 1 - Sedentary (little to no exercise + work a desk job)
            2: 1.375, # 2 - Lightly Active (light exercise 1-3 days / week)
            3: 1.55,  # 3 - Moderately Active (moderate exercise 3-5 days / week)
            4: 1.725, # 4 - Very Active (heavy exercise 6-7 days / week)
            5: 1.9    # 5 - Extremely Active (very heavy exercise, hard labor job, training 2x / day)
        }
        
        return self.bmr * factor.get(self.activity_level)
    
    def get_daily_water_intake(self):
        
        '''Cálculo del consumo de agua diario en función del metabolismo basal y del factor de actividad física'''

        return 0.96 * self.get_tdee()

def getUser(username):
    file_name= "./app/user/users/"+username+"_data.json"
    try:
        with open(file_name, 'r') as f:
            json_user = json.load(f)
    except:
        print(f"User {username} doesn't exist")
        return None

    user = json_user #es un DICT no un User
    #user = json2User(json.loads(json_user)) # para la CLASE User

    return user

def json2User(json_user):
    #TODO añadir todos los params aquí o usar esto:
    # https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
    # o guardar los objetos con pickle en vez de en json
    user = json.loads(json_user, object_hook=lambda d: SimpleNamespace(**d))
    
    return user
   

def createNewUser(new_user_data, serialize  = True):
    new_user = User(username=new_user_data['username'],
                    name= new_user_data['name'],
                    age= new_user_data['age'],
                    sex = new_user_data['sex'],
                    weight = new_user_data['weight'],
                    height = new_user_data['height'],
                    body_type = new_user_data ['body_type'],
                    activity_level = new_user_data['activity_level'],
                    liked_ingredients = new_user_data['liked_ingredients'],
                    objective = new_user_data['objective'],
                    using_scale = new_user_data['using_scale'],
                    serialize  = serialize )
    return new_user
    
def main():
    print("Clase usuario")

if __name__ == "__main__":
  main()

