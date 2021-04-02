class User:
    
    '''Esta clase define un perfil de un usuario de nuestro sistema, con todos los datos necesarios para generar recomendaciones.
        Además, almacena los parámetros necesarios para la monitorización de su estado físico a través de la bascula Xiaomi.'''
    
    def __init__(self, name, sex, age, height, weight, 
                 body_type, activity_level, liked_ingredients, disliked_ingredients = None,
                 user_objective, using_scale = False, scale_parameters):
        
        '''Constructor de la clase de usuario, scale_parameters es un dict con los parámetros de la báscula'''
        
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.body_type = body_type # Ectomorfo, mesomorfo, o endomorfo
        self.activity_level  # Nivel de actividad física del usuario (de los definidos en el Excel)
        self.liked_ingredients = liked_ingredients
        self.disliked_ingredients = disliked_ingredients
        self.user_objective = user_objective # Ganar masa muscular, mantenerse, adelgazar
    
        if using_scale == False:
            
            self.weight = weight
            self.bmi = self.get_bmi()
            self.bmr = self.get_bmr()
            self.tdee= self.get_tdee()
            self.water_intake = self.get_daily_water_intake()
        
        elif using_scale == True:
            
            self.weight = scale_parameters["weight"]
            self.bmi = scale_parameters["bmi"]
            self.bmr = scale_parameters["bmr"] 
            self.body_fat = scale_parameters["body_fat"]
            self.visceral_fat = scale_parameters["visceral_fat"]
            self.muscle_mass = scale_parameters["muscle_mass"]
            self.body_water = scale_parameters["body_water"]
            self.bone_mass = scale_parameters["bone_mass"]
            self.tdee= self.get_tdee()
            self.water_intake = self.get_daily_water_intake()


    
    def get_bmi(self):
        
        '''Cálculo del BMI (índice de masa corporal) para el caso de no conectar con la báscula'''

        return self.weight / (self.height ** 2)
        
    def get_bmr(self):
        
        '''Cálculo del BMR (metabolismo basal) para el caso de no conectar con la báscula'''
        if self.sex == "Hombre":
            return 66,473 + (13,751 x self.weight) + (5,0033 x self.height) - (6,7550 x self.age)
        elif self.sex == "Mujer":
            return 655,1 + (9,463 x self.weight) + (1,8 x self.height) - (4,6756 x self.age)
        
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
    
    def get_daily_water_intake():
        
        '''Cálculo del consumo de agua diario en función del metabolismo basal y del factor de actividad física'''

        return 0.96 * get_tdee()
    
    
def main():
    print("Clase usuario")

if __name__ == "__main__":
  main()

