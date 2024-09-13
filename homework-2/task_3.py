number = int(input("Input natural number not exceeding 10: "))

if number > 10 or number < 1:
    print("Wrong input")
    exit(1)

if number % 2 == 0:
    print(2, end = ' ')
if number % 3 == 0:
    print(3, end=' ')
if number % 5 == 0:
    print(5, end=' ')
if number % 7 == 0:
    print(7, end=' ')