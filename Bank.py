#Переменные
pin = int(input("Enter your pin-code: "))
print("Pin-code saved!")

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
    menu_input = input("Enter your choice: ")

    if menu_input == "1":
        print_balance()

    elif menu_input == "2":
        pin_check = int(input("Enter your pin code: "))
        if pin_check != pin:
            print("Wrong pin code!")
        else:
            withdraw = int(input("Enter your withdraw amount: "))
            if withdraw > balance:
                print("Wrong withdraw amount!")
            if withdraw <= balance:
                balance = balance - withdraw
                print_balance()

    elif menu_input == "3":
        pin_check = int(input("Enter your pin code: "))
        if pin_check != pin:
            print("Wrong pin code!")
        else:
            deposit = int(input("Enter your deposit amount: "))
            balance = balance + deposit
            print(f"Deposit successful!")
            print_balance()

    if menu_input == "4":
        print('Goodbye!')
        break
    else:
        print("Please enter a valid choice!")

