from datetime import datetime

def car(make, year=datetime.now().year, **kwargs):
    print('Car make:', make)
    print('Manufacturing year:', year)

    if kwargs:
        print('Special configurations:')
        for key, value in kwargs.items():
            print(f'\t{key}: {value}')

car('Cadillac', 1999, Engine='Northstar', Cylinders='V8')
print()
car('Mercedes', 1997, **{'Model': '600 SEL', 'Body': 'W140', 'Displacement': '5987 cc', 'Top speed': '250 km/h'})