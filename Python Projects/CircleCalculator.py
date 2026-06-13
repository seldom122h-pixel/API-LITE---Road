import math

while True:
    try:
        print('----------------------')
        radius = float(input('Enter circle radius: '))
        break
    except ValueError:
        print("Enter a valid value!")
        continue

CircleC = 2 * math.pi * radius
CircleS = math.pi * pow(radius, 2)

print('----------------------')
print(f"Circle lenght: {round(CircleC, 2)}")
print(f"Сircle area: {round(CircleS, 2)}")
print('----------------------')

print( f"Goodbye!   ")