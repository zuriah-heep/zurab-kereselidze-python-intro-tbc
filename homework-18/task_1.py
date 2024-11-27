with open("small.txt", "w") as file:
    pass
with open("high.txt", "w") as file:
    pass

with open("data.txt", "r") as data, open("small.txt", "a") as small, open("high.txt", "a") as high:
    for line in data:
        _, _, amount, price = line.strip().split(',')
        if int(amount) * float(price) < 10:
            small.write(line)
        else:
            high.write(line)