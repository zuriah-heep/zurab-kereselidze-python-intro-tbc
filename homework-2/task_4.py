speed = float(input("Enter vehicle's speed in km/h: "))

if speed < 0:
    exit(1)

if speed > 120:
    print("The vehicle is VERY FAST")
elif speed > 60:
    print("The vehicle is FAST")
elif speed > 30:
    print("The vehicle is MODERATE")
else:
    print("The vehicle is SLOW")