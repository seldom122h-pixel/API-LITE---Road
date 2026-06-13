#Переменные
name = input('Hi! Enter your name >> ')

while True:
    try:
        pin = int(input("Enter your pin-code: "))
        print("Pin-code saved!")
        break
    except ValueError:
        print('Enter a number!')
        continue

balance = 1000

#Вывести баланс
def print_balance():
    global balance
    print(f"Your balance : {balance} USD")

while True:
    menu_str = """
--------- Bank | Menu ---------  
    1. View balance
    2. Withdraw money
    3. Deposit
    4. Exit the Bank
-------------------------------
    """
    print(menu_str)

    try:
        menu_input = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if menu_input == 1:
        print_balance()

    elif menu_input == 2:
        pin_check = int(input("Enter your pin code: "))
        if pin_check != pin:
            print("Wrong pin code!")
        else:
            try:
                withdraw = int(input("Enter your withdraw amount: "))
                if withdraw > balance:
                    print("Wrong withdraw amount!")
                if withdraw <= balance:
                    balance = balance - withdraw
                    print_balance()
                    
            except ValueError:
                print("Please enter a number")
                continue

    elif menu_input == 3:
        pin_check = int(input("Enter your pin code: "))
        if pin_check != pin:
            print("Wrong pin code!")
        else:
            deposit = int(input("Enter your deposit amount: "))
            balance = balance + deposit
            print("Deposit successful!")
            print_balance()

    elif menu_input == 4:
        print(f'Goodbye {name}!')
        break
    else:
        print("Please enter a valid choice!")