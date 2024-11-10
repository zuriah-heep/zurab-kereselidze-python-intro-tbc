a = int(input('Enter a: '))
b = int(input('Enter b: '))

if not 0 < a <= 10000 or not 0 < b <= 10000:
    print('Input number(s) out of range')
    exit(1)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return int(a * b / gcd(a, b))


def main():
    print(f'LCM of {a} and {b} is {lcm(a, b)}.')

if __name__ == "__main__":
    main()