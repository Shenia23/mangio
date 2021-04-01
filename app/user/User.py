class User:
    
    '''Esta clase define un perfil de un usuario de nuestro sistema, con todos los datos necesarios para generar recomendaciones.
        Además, almacena los parámetros necesarios para la monitorización de su estado físico a través de la bascula Xiaomi.'''
    
    def __init__(self, name):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.body_type = body_type # Ectomorfo, mesomorfo, o endomorfo
        self.activity_level  # Nivel de actividad física del usuario (de los definidos en el Excel)
        self.liked_ingredients = liked_ingredients
        self.disliked_ingredients = disliked_ingredients
        self.user_objective = user_objective # Ganar masa muscular, mantenerse, adelgazar
        
    def set_xiaomi_parameters(self, ):
        self.weight = weight
        self.bmi = bmi
        self.bmr = bmr 
        self.body_fat = body_fat
        self.visceral_fat = visceral_fat
        self.muscle_mass = muscle_mass
        self.body_water = body_water
        self.bone_mass = bone_mass
        
    def get_tdee(self):
        
        '''Cálculo del consumo calórico total diario en función del metabolismo basal y del factor de actividad física'''

        factor= { #Factor de ajuste correspondiente al nivel de actividad física
            1: 1.2,   # 1- Sedentary (little to no exercise + work a desk job)
            2: 1.375, # 2- Lightly Active (light exercise 1-3 days / week)
            3: 1.55,  # 3- Moderately Active (moderate exercise 3-5 days / week)
            4: 1.725, # 4- Very Active (heavy exercise 6-7 days / week)
            5: 1.9    # 5-Extremely Active (very heavy exercise, hard labor job, training 2x / day)
        }
        
        return self.bmr * factor.get(self.activity_level)
    
    def get_daily_water_intake():
        '''Cálculo del consumo de agua diario en función del metabolismo basal y del factor de actividad física'''

        return 0.96 * get_tdee()
    
    
def main():
    print("Clase usuario")

if __name__ == "__main__":
  main()

