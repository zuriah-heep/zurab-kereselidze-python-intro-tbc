from random import randint
list = []
for i in range(50):
    rand = randint(1, 30)
    list.append(rand)

new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)

print('List -', new_list)
print('Length -', len(new_list))