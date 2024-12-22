class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return f'Person - {self._name}, {self._age}'

def main():
    z = Person('Zura', 40)
    print(z.get_info())
    g = Person('Giorgi', 35)
    print(g.get_info())

    print(z.name)

if __name__ == '__main__':
    main()