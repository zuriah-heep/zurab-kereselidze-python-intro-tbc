text = input('Please enter some text - ').lower().strip()
new_text = ''

for i in text:
    if i.isalnum():
        new_text += i

if new_text == new_text[::-1]:
    print('Is palindrome')
else:
    print('Is not palindrome')