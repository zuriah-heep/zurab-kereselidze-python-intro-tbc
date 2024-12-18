class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, v):
        if v < 0:
            raise ValueError("Age can not be negative")
        self._age = v

    @property
    def get_info(self):
        return f'Person - {self._name}, {self._age}'

def main():
    z = Person('Zura', 40)
    print(z.get_info)
    print(z.name)

    z.name = 'Giorgi'
    z.age = 35
    print(z.get_info)

    print(z.name)

if __name__ == '__main__':
    main()