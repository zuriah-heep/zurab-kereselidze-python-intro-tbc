action = input('Enter action (e/d): ')

while action not in 'ed':
    action = input('Please enter "e" or "d" for action: ')

text = input('Enter text: ')
new_text = ''

line1 = 'qwertyuiop'
line2 = 'asdfghjkl'
line3 = 'zxcvbnm'

for i in text:
    if i in line1:
        if action == 'e':
            new_text += line1[line1.index(i) + 1 - len(line1)]
        else:
            new_text += line1[line1.index(i) - 1]
    elif i in line2:
        if action == 'e':
            new_text += line2[line2.index(i) + 1 - len(line2)]
        else:
            new_text += line2[line2.index(i) - 1]
    elif i in line3:
        if action == 'e':
            new_text += line3[line3.index(i) + 1 - len(line3)]
        else:
            new_text += line3[line3.index(i) - 1]
    else:
        new_text += i

print(new_text)