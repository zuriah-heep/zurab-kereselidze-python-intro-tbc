class ListExtended(list):
    def __init__(self, *args):
        super().__init__(*args)

    def min(self):
        return min(self)

    def max(self):
        return max(self)

def main():
    list1 = ListExtended()
    list1.append(5)
    list1.append(15)
    list1.append(-5)
    list1.append(2)
    print(list1)
    print(min(list1))
    print(max(list1))

    list2 = ListExtended([5, 6])
    list2.append(5)
    list2.append(15)
    list2.append(-5)
    list2.append(2)
    print(list2)
    print(list2.min())
    print(list2.max())

if __name__ == '__main__':
    main()