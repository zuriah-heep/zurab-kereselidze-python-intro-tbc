text = input('Please enter some text - ').lower().strip()
new_text = ''
palindrome = True

for i in text:
    if 96 < ord(i) < 123:
        new_text += i

for i in range(int(len(new_text)/2)):
    if new_text[i] !=  new_text[-i - 1]:
        print('Is not palindrome')
        palindrome = False
        break

if palindrome:
    print('Is palindrome')