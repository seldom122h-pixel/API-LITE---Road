name = input('Enter your name: ')
try:
    age = int(input('Enter your age: '))
    now_year = int(input('Enter current year: '))
    if now_year > 2026:
        print('Please enter a valid year!')
    else:
        BirD = now_year - age
        print(f"{name}, you were born in {BirD}")
except ValueError:
    print('Please enter a valid number!')