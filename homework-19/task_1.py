import json

file_name = "homework_1.json"
avg_salary = {}

try:
    with open(file_name, 'r') as file:
        data = json.load(file)

    for key, department in data.items():
        total, amount = 0, 0

        try:
            if not department["employees"]:
                avg_salary[department.get("name", key)] = "No information about employees"
                continue

            for employee in department["employees"]:
                try:
                    total += float(employee["salary"])
                    amount += 1
                except KeyError:
                    print("Missing 'salary' key in", key)
                except (ValueError, TypeError) as er:
                    print(f"{er}.", employee.get("name", "Unknown employee"), "salary is missing")

            try:
                avg_salary[department["name"]] = str(total / amount)
            except KeyError:
                print("Missing 'name' key in", key)
            except ZeroDivisionError:
                print("Division by zero in", department["name"])
                avg_salary[department["name"]] = "No information about salaries"
        except KeyError:
            print("Missing 'employees' key in", department.get("name", key))

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as ex:
    print("Error: ", ex)

print(avg_salary)

with open('salary.json', 'w') as file:
    json.dump(avg_salary, file, indent = 2)