def temperature_converter(degree, unit):
    if unit.lower() == 'c':
        return f'{degree * 9/5 + 32} F'
    elif unit.lower() == 'f':
        return f'{(degree - 32) * 5/9} C'
    else:
        return 'Wrong unit'


def main():
    print(temperature_converter(0, 'c'))
    print(temperature_converter(32, 'f'))
    print(temperature_converter(-40, 'c'))
    print(temperature_converter(-40, 'f'))
    print(temperature_converter(-40, 'k'))

if __name__ == "__main__":
    main()