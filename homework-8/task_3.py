date = input('Please enter date - ').strip()

day, rest = date.split('T')
day = '-'.join(day.split('-')[::-1])
time, zone = rest.split('.')
time = time.split(':')
time[0] = int(time[0])
if time[0] > 12:
    time[0] = time[0] - 12
time[0] = str(time[0])
time = ':'.join(time)

for sign in '-+':
    if sign in zone:
        zone = zone.split(sign)[1]
        break
zone = sign + str(int(zone.split(':')[0])) + (':' + zone.split(':')[1]).replace(':00','')

print(day, time, zone)

"""
Input-ის ფორმატიდან გამომდინარე რათქმაუნდა შეიძლებოდა split/join-ის გარეშეც გაკეთება 
მხოლოდ ინდექსებით, მაგრამ ლექციაზე ახსნილიდან გამომდინარე ჩავთვალე რომ ასე უკეთესი იქნებოდა.
"""