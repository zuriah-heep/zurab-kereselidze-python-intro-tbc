from random import randrange

def main():
    num_count = {'even': 0, 'odd': 0}
    for _ in range(100):
        num = randrange(1000)
        if num % 2 == 0:
            num_count['even'] += 1
        else:
            num_count['odd'] += 1

if __name__ == '__main__':
    main()