def sort(a, b):
    c = []
    for i in a:
        # ვქმნი b.copy() რომ b-ს ცვლილებამ შიდა ციკლზე არ იმოქმედოს
        for j in b.copy():
            if j <= i:
                c.append(j)
                b.remove(j)
            else:
                break
        c.append(i)
    #ვამატებ დარჩენილ b-ს წევრებს
    for i in b:
        c.append(i)
    return c

def main():
    print(sort([1,  3, 10], [0, 4,7, 9]))
    print(sort([0, 4, 7, 9], [1,  3, 10]))
    print(sort([-17, -5, 0, 6, 50], [0, 0, 1, 6]))
    print(sort([-5, -5, 5, 10], [-6, -4, 0, 8, 12]))

if __name__ == "__main__":
    main()