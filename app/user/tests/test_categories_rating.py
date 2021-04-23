

preferences= [
        {
            "categories": [
                "Carne",
                "Arroz"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Pescado",
                "Patatas"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Carne",
                "Pasta"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Pollo",
                "Arroz"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Legumbres",
                "Arroz"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Pollo",
                "Verduras"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Pasta",
                "Verduras"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Carne",
                "Patatas"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Pescado",
                "Arroz",
                "Verduras"
            ],
            "rating": "super"
        },
        {
            "categories": [
                "Verduras",
                "Huevos",
                "Patatas"
            ],
            "rating": "super"
        },
        {
            "categories": [
                "Pescado",
                "Legumbres",
                "Patatas"
            ],
            "rating": "super"
        },
        {
            "categories": [
                "Verduras",
                "Pasta"
            ],
            "rating": "super"
        }
    ]
def get_ratings(preferences):
    
    ratings = {
    "Carne":0,
    "Pollo":0,
    "Pescado":0,
    "Legumbres":0,
    "Verduras":0,
    "Patatas":0,
    "Arroz":0,
    "Pasta":0,
    "Huevos":0
    }
    
    for preference in preferences:
        
        for category in preference["categories"]:
            
            if preference["rating"] == "like":
                
                ratings[category] += 1/len(preference["categories"])
                
            elif preference["rating"] == "nope":
                
                ratings[category] -= 1/len(preference["categories"])

            
            elif preference["rating"] == "super":
                
                ratings[category] += 1.1 * 1/len(preference["categories"])

    
    
    return ratings       

                
print(get_ratings(preferences))