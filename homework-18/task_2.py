import json

dict_for_json = {}
data = []
user_purchases = {}
product_amounts = {}
max_amounts = {}

with open("data.txt", "r") as file:
    for line in file:
        user, product, amount, price = line.strip().split(',')
        amount, price = int(amount), float(price)

        data.append([user, product, amount, price])

        max_amounts[user] = max_amounts.get(user, amount)
        if amount > max_amounts[user]:
            max_amounts[user] = amount

        user_purchases[user] = user_purchases.get(user, 0) + amount * price
        product_amounts[product] = product_amounts.get(product, 0) + amount

dict_for_json['users with max amount per one purchase'] = [key for key, val in max_amounts.items() if val == max(max_amounts.values())]
dict_for_json['richest users'] = [key for key, val in user_purchases.items() if val == max(user_purchases.values())]
dict_for_json['mean of purchases'] = [sum(i[2] * i[3] for i in data) / len(data)]
dict_for_json['mean of amounts'] = [sum(i[2] for i in data) / len(data)]
dict_for_json['highest selling products'] = [key for key, val in product_amounts.items() if val == max(product_amounts.values())]

for key, val in dict_for_json.items():
    if len(val) == 1:
        dict_for_json[key] = val[0]

with open('stats.json', 'w') as file:
    json.dump(dict_for_json, file, indent=4)