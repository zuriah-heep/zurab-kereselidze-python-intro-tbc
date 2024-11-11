n = int(input("Please enter a whole number between 10 and 5432 - "))

if not 10 <= n <= 5432:
    print("You entered a wrong number")
    exit(1)

amount = 0
for i in range(1, n + 1):
    if i % 13 == 0:
        print(i, end = ' ')
        amount += 1

print()
print("Amount:", amount)