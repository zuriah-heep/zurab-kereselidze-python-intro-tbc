for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', str(j * i).ljust(2), end = '   ')
    print()