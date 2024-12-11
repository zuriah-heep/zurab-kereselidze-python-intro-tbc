class Inset:
    def __init__(self):
        self.my_list = []

    def insert(self, element):
        if element not in self.my_list:
            self.my_list.append(element)

    def member(self, element):
        return element in self.my_list

    def remove(self, element):
        try:
            self.my_list.remove(element)
        except ValueError:
            print('ვერ ვიპოვნე')

    def __str__(self):
        self.my_list.sort()
        return ' '.join(map(str, self.my_list))


def main():
    obj = Inset()
    obj.insert(5)
    obj.insert(1)
    obj.insert(-5)
    obj.insert(50)
    obj.insert(-5)
    obj.remove(4)
    obj.remove(50)
    print(obj)
    print(obj.member(5))
    print(obj.member(4))

if __name__ == '__main__':
    main()