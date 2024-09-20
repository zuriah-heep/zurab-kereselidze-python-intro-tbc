from datetime import datetime

_weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

_year = int(input('Enter your year of birth: '))
_month = int(input('Enter your month of birth in number: '))
_day = int(input('Enter your birth day of the month: '))

_weekday = _weekdays[datetime(_year, _month, _day).weekday()]

print(_weekday)