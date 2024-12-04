import json
from itertools import combinations

dish = input("Which dish would you like to prepare? - ").strip().title()

with open("homework_1_markets.json", "r") as markets_file, open("homework_1_recipes.json", "r") as recipes_file:
    recipes = json.load(recipes_file)
    markets = {key: set(value) for key, value in json.load(markets_file).items()}

try:
    ingredients = set(recipes[dish]["ingredients"])
    market_names = list(markets.keys())

    found = False
    output = "You cannot prepare this dish in this town."
    combination_size = 1

    while not found and combination_size <= len(market_names):
        for key_groups in combinations(market_names, combination_size):
            set_union = set()
            for key in key_groups:
                set_union |= markets[key]
            if ingredients.issubset(set_union):
                output = f"Markets to visit: {', '.join(key_groups)}."
                found = True
                break
        combination_size += 1

    print(output)

except KeyError:
    print(f"Error: No '{dish}' in recipes.")
except Exception as ex:
    print("Error:", ex)