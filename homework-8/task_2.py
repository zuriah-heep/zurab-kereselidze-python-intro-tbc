str1 = input('Please enter string 1 - ').lower()
str2 = input('Please enter string 2 - ').lower()

for i in str1:
    if i in str2:
        str2 = str2.replace(i, '', 1)
    else:
        break

if str2 == '':
    print('YES')
else:
    print('NO')