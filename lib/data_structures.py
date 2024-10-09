spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [each_food["name"] for each_food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [each_food for each_food in spicy_foods if each_food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for each_food in spicy_foods:
        print(f'{each_food["name"]} ({each_food["cuisine"]}) | Heat Level: {each_food["heat_level"] * "🌶"}')
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    gen = [each_food for each_food in spicy_foods if each_food["cuisine"] == cuisine]
    return gen[0]

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))
    pass

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food["heat_level"]
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
