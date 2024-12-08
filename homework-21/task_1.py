import json

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class Department:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def average_salary(self):
        if not self.employees:
            return "No information about employees"

        try:
            avg_salary = sum([float(employee.salary) for employee in self.employees]) / len(self.employees)
        except ZeroDivisionError:
            print("Division by zero in", self.name)
        except KeyError:
            print("Missing 'employees' key in", self.name)

        return avg_salary


    def max_salary(self):
        if not self.employees:
            return "No information about employees"
        return max([float(employee.salary) for employee in self.employees])

    def min_salary(self):
        if not self.employees:
            return "No information about employees"
        return min([float(employee.salary) for employee in self.employees])

    def positions(self):
        positions = {}
        for employee in self.employees:
            positions[employee.position] = positions.get(employee.position, 0) + 1
        return positions


def main():
    filename = 'homework_1.json'
    departments = {}

    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        for key, department in data.items():
            # შევქმნათ დეპარტამენტის ობიექტი
            departments[key] = Department(department['name'], department['description'])

            # შევქმნათ თანამშრომლების ობიექტები და დავამატოთ დეპარტამენტის ობიექტს
            for employee in department['employees']:
                employee_object =  Employee(employee['name'], employee['position'], employee['salary'])
                departments[key].add_employee(employee_object)

            print()
            print(departments[key].name)
            print('\tAverage salary:', departments[key].average_salary())
            print('\tHighest salary:', departments[key].max_salary())
            print('\tLowest salary:', departments[key].min_salary())
            print('\tPositions:', departments[key].positions())

    except FileNotFoundError:
        print(f'File "{filename}" not found.')
    except Exception as ex:
        print('Error: ', ex)


    # ახლა Department 3-ს ჩვენით მივამატოთ თანამშრომლები
    employees = [Employee('Zurab Kereselidze', 'Senior Python Engineer', 130),
                Employee('Mariam Migriauli', 'Senior Python Engineer', 140),
                Employee('Tornike Chikhladze', 'Senior Python Engineer', 150),
                Employee('Irakli Margvelashvili', 'Senior Python Engineer', 160),
                Employee('Aleksandra Shalibashvili', 'Senior Python Engineer', 170),
                Employee('Guranda Jikia', 'Senior Python Engineer', 180),
                Employee('Irakli Sakhvadze', 'Senior Python Engineer', 190),
                Employee('Tinatin Tsakadze', 'Mentor', 300),
                Employee('Mikheil Lomidze', 'Mentor', 330)]

    for employee in employees:
        departments['department_3'].add_employee(employee)

    print()
    print(departments['department_3'].name, 'after adding employees')
    print('\tAverage salary:', departments['department_3'].average_salary())
    print('\tHighest salary:', departments['department_3'].max_salary())
    print('\tLowest salary:', departments['department_3'].min_salary())
    print('\tPositions:', departments['department_3'].positions())

if __name__ == '__main__':
    main()