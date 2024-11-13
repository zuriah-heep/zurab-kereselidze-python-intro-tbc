from random import randint
list = []
for i in range(50):
    rand = randint(1, 30)
    for j in range(rand):
        list.append(rand)

print('List -', list)
print('Length -', len(list))