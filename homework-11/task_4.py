import timeit

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
    def iter():
        gcd_iter(a, b)

    def rec():
        gcd_rec(a, b)

    result_rec = timeit.timeit(rec, number=1000)
    print("Time elapsed for recursion executed 100000 times: ", result_rec)

    result_iter = timeit.timeit(iter, number=1000)
    print("Time elapsed for iteration executed 100000 times: ", result_iter)

    if result_rec < result_iter:
        print('Recursion is faster')
    elif result_rec > result_iter:
        print('Iteration is faster')
    else:
        print('Both methods require same time')

if __name__ == "__main__":
    main()