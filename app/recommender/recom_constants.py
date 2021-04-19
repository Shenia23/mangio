'''
File with all the constant values required for the recommender
'''

BREAKFAST = 'desayuno'
LUNCH = 'comida'
DINNER = 'cena'
SNACK = 'snack'
MERIENDA = 'merienda'

CATEGORIES = {
    BREAKFAST:  ['Desayuno','Entrante'],
    LUNCH:      ['Plato principal','Entrante','Acompañamiento'],
    SNACK:      ['Merienda','Cumpleaños','Postre'],
    MERIENDA:   ['Merienda','Cumpleaños','Postre'],
    DINNER:     ['Cena','Entrante','Plato principal','Acompañamiento']
}

TDEE_MULTIPLIERS = {
    BREAKFAST:  0.2,
    SNACK:      0.1,
    MERIENDA:   0.1,
    LUNCH:      0.35,
    DINNER:     0.25
}

FOOD_TYPES = [BREAKFAST, LUNCH, DINNER, SNACK, MERIENDA]
FIXED_FOOD_TYPES = [BREAKFAST, SNACK, MERIENDA]

#OBJECTIVES
GAIN = 3
MANTAIN = 2
LOSS = 1

#MACROS
KCAL = 'energia'
CARBS = 'carbohidratos'
PROTS = 'proteina'
GRASAS = 'grasa'

TARGET_MACROS = [KCAL, GRASAS, PROTS, CARBS]
CAL_GRAM = 'calorias_por_gramo'

MACROS = { 
    GRASAS: {
        GAIN: [15,25],
        MANTAIN: [25,35],
        LOSS: [30,40],
        CAL_GRAM: 9
    },
    PROTS: {
        GAIN: [25,35],
        MANTAIN: [25,35],
        LOSS: [40,50],
        CAL_GRAM: 4
    },
    CARBS: {
        GAIN: [40,60],
        MANTAIN: [30,50],
        LOSS: [10,30],
        CAL_GRAM: 4
    }
}