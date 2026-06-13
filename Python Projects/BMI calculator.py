def line():
    print('---------------------------')


while True:
    menu = """
    -= BMI calculator =-

1. Calculate BMI
2. Exit
---------------------------"""
    print(menu)
    try:
        cmd = int(input("Enter your choice >> "))
    except ValueError:
        print('Enter valid value!')
        continue

    if cmd == 1:
        try:
            weight = float(input('Enter your weight (in kg)>> '))
            height = float(input('Enter your height (in meters) >> '))
            BMI = weight / (height ** 2)

            line()
            print(f"Your BMI: {round(BMI, 2)}")
            line()

            if BMI < 18.5:
                category = "Underweight \ Недостаточный вес"
            elif BMI < 25:
                category = "Normal weight \ Нормальный вес "
            elif BMI < 30:
                category = "Overweight \ Избыточный вес "
            elif BMI < 35:
                category = "Obesity Class I \ Ожирение I степени "
            elif BMI < 40:
                category = "Obesity Class II \ Ожирение II степени "
            else:
                category = "Obesity Class III \ Ожирение III степени"

            print(f"Category: {category}")
            line()

        except ValueError:
            print('Enter valid value!')
            continue
        

    elif cmd == 2:
        print('Goodbye!')
        exit()
    else:
        print('Enter a valid number!')