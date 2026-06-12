print("""
   -Welcome to the Mini Project Calculator- 
    """)

input("Press any key to continue...")

def line():
    print("----------------------------------------------")

while True:
    try:
        input_num = float(input("Enter a first number >>> "))
        input_num_2 = float(input("Enter a second number >>> "))
    except ValueError:
        print("Please enter a number")
        continue

    print("""
             - Opertions -
----------------------------------------------       
1. Adition / Сложение
2. Subtraction / Вычетание
3. Multiplication / Умножение
4. Division / Деление
5. Involution / Возведение в степень
6. Exit a calculator / Выход из калькулятора
---------------------------------------------- """)

    operation_cmd = input("Enter a operation >>> ")

    line()

    match operation_cmd:
        case "1":
            result = input_num + input_num_2
        case "2":
            result = input_num - input_num_2
        case "3":
            result = input_num * input_num_2
        case "4":
            result = input_num / input_num_2 if input_num_2 != 0 else None
        case "5":
            result = input_num ** input_num_2
        case "6":
            exit()
        case _:
            print("Invalid choice")

    if result is None:
        print("You cannot divide by zero")
    else:
        print(f"Result: {result}")

    line()