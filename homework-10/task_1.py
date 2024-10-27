def vowels(text):
    vow = 'aeiou'
    amount = 0
    for char in text.lower():
        if char in vow:
            amount += 1
    return amount

print(vowels('Python'), vowels('qwertYUIOPasdfgHJKLzxcvBnm'), vowels('My name is Zurab.'))