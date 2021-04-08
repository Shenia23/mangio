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

#OBJECTIVES
GAIN = 0
MANTAIN = 1
LOSS = 2

#MACROS
CARBS = 'carbohidratos'
PROTS = 'proteinas'
GRASAS = 'grasas'

MACROS = { 
    CARBS: {
        GAIN: [40,60],
        MANTAIN: [30,50],
        LOSS: [10,30],
        "column": "grasa_cals_pctg"
    },
    PROTS: {
        GAIN: [25,35],
        MANTAIN: [25,35],
        LOSS: [40,50],
        "column": "proteina_cals_pctg"
    },
    GRASAS: {
        GAIN: [15,25],
        MANTAIN: [25,35],
        LOSS: [30,40],
        "column": "carbos_cals_pctg"
    }
}