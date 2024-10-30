a = int(input('Enter a: '))
b = int(input('Enter b: '))

if not 0 < a <= 10000 or not 0 < b <= 10000:
    print('Input number(s) out of range')
    exit(1)

def gcd_rec(a, b):
    if b == 0:
        return a
    return gcd_rec(b, a%b)

def gcd_iter(a, b):
    m = min(a, b)
    while m > 0:
        if a % m == 0 and b % m == 0:
            return m
        m -= 1


def main():
    print(f'GCD of {a} and {b} is {gcd_rec(a, b)}. (using recursion method)')
    print(f'GCD of {a} and {b} is {gcd_iter(a, b)}. (using iteration method)')

if __name__ == "__main__":
    main()