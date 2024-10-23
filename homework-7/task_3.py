text = input('Please enter a word - ').strip()

characters = text[-1] + text[0]
if len(text) % 2:
    characters += text[int(len(text) / 2)]
else:
    characters += text[int(len(text) / 2) - 1] + text[int(len(text) / 2)]

index = 0
while index < len(characters):
    count = 0
    while count < 5:
        print(characters[index], end = ' ')
        count += 1
    index += 1
    print()

"ეს რადგან while-ის გამოყენებით უნდა გაგვეკეთებინა"