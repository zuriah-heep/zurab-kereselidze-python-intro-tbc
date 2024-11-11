def fibonachi(n):
    if not isinstance(n, int):
        return

    for i in range(n):
        if i == 0 or i == 1:
            yield i
            prev1 = 1
            prev2 = 0
        else:
            number = prev1 + prev2
            yield number
            prev2 = prev1
            prev1 = number

def main():
    for n in (0, 2, 5, 20):
        fib_nums = fibonachi(n)
        print('First', n, 'numbers -', end=' ')
        for num in fib_nums:
            print(num, end = ' ')
        print()
        for _ in fib_nums:
            print('Will not print this part as generator already has reached the end in previous for loop')

if __name__ == "__main__":
    main()