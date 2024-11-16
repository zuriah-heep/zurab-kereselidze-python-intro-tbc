def main():
    my_string = input('Please input string: ')
    char_counter = {}

    for char in my_string:
        char_counter[char] = char_counter.get(char, 0) + 1

    for key, val in char_counter.items():
        print(key, '-', val)

if __name__ == '__main__':
    main()