n = input('Enter a non-negative whole number below 10000: ')

if not 0 <= int(n) < 10000:
    print('Entered number does not meet the requirement.')
    exit(1)

_sum = 0
_reversed = ''
index = len(n)

while index > 0:
    index -= 1
    _reversed += n[index]
    _sum += int(n[index])

print('reversed number is', int(_reversed))
print('sum of digits:', _sum)