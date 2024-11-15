from random import randint


def main():
    list_1, list_2, list_3 = [[randint(0,100) for _ in range(30)] for _ in range(3)]
    print(list(map(lambda x, y, z: x + y + z, list_1, list_2, list_3)))

if __name__ == "__main__":
    main()