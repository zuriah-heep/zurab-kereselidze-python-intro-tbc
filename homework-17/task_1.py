def collatz(n):
    my_list = []
    while n != 1:
        my_list.append(n)
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3 * n + 1
    my_list.append(1)
    return my_list

def collatz_cached(n):
    key = n
    my_list = [n]
    while n not in cache:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        my_list.append(n)
    my_list += cache[n]
    cache[key] = my_list[1:]
    return my_list

def main():
    seq = [1, 3, 16, 32, 400, 200, 201]
    print("Using collatz(n)")
    for n in seq:
        print(n, "-", collatz(n))
    print()

    global cache
    cache = {1: []}
    print("Using collatz_cached(n)")
    for n in seq:
        print(n, "-", collatz_cached(n))
        print(f"cache[{n}]", "-", cache[n])


if __name__ == "__main__":
    main()