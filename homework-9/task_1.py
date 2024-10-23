n = int(input('Enter a natural number greater than 1: '))

if n <= 1:
    print('Entered number does not meet the requirement.')
    exit(1)

_sum = 0
for i in range(1, n + 1):
    _sum += (-1) ** (i - 1) / (2 * i - 1)
x = 4 * _sum
print(x)

"""
ეს არის π-ს გამოსათვლელი ფორმულა. რაც უფრო დიდია n მით უფრო მეტი ციფრის სიზუსტით ემთხვევა შედეგი π-ს.
თუ n = 10^k მაშინ ჯამის პირველი k ციფრი დაემთხვევა π-ს.
"""