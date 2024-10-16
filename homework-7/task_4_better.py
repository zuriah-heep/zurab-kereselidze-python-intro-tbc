action = input('Enter action (e/d): ')

while action not in 'ed':
    action = input('Please enter "e" or "d" for action: ')

text = input('Enter text: ')
new_text = ''
lines = ('qwertyuiop', 'asdfghjkl', 'zxcvbnm')

for i in text:
    for line in lines:
        if i in line:
            if action == 'e':
                new_text += line[line.index(i) + 1 - len(line)]
            else:
                new_text += line[line.index(i) - 1]
            break
    else:
        new_text += i

print(new_text)