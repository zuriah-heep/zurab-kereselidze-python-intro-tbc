text = input('Please enter a word - ').strip()

for i in text:
    if i.lower() not in 'aeiou':
        print(i, end = ' ')