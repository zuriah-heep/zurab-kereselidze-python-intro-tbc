def main():
    from random import randint

    numbers = [str(randint(10, 1000000000)) for _ in range (100)]
    longest_number = max(numbers, key = len)
    shortest_number = min(numbers, key = len)
    numbers_ascending = [int(n) for n in sorted(numbers, key = len)]
    numbers_descending = [int(n) for n in sorted(numbers, key = len, reverse = True)]

    print('The longest number -', longest_number)
    print('The shortest number -', shortest_number)
    print('Numbers ascending by length -', numbers_ascending)
    print('Numbers descending by length -', numbers_descending)

if __name__ == "__main__":
    main()