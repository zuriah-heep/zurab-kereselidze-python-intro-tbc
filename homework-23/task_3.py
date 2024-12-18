class Student:
    def __init__(self, name):
        self._name = name
        self._scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print('არასწორი ქულა')

    def get_average(self):
        try:
            return sum(self._scores) / len(self._scores)
        except ZeroDivisionError as er:
            return f'{er}: scores list is empty.'

    def get_scores(self):
        return self._scores

def main():
    z = Student('Zura')
    z.add_score(50)
    z.add_score(75)
    z.add_score(100)
    print(z.get_average())
    print(z.get_scores())

    g = Student('Giorgi')
    print(g.get_average())
    print(g.get_scores())

    #ეს მოგვცემს შეცდომას
    #print(z.name, g.name)

if __name__ == '__main__':
    main()