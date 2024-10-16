text = input('Please enter text - ')

for i in range(1, len(text), 2):
    if text[i] != 'e':
        print(text[i], end = ' ')