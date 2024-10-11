for i in range(1, 10):
    for j in range(1, 10):
        print(j, '*', i, '=', j * i, end = '   ')
        if j == i:
            break
    print()