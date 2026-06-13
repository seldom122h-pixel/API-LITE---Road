import datetime as dt
import random
import string

def get_date():
    print('-------------------------------')
    print(f" Today's date : {dt.datetime.now().date()}")
    print('-------------------------------')

def get_time():
    print('-------------------------------')
    print(f"Time : {dt.datetime.now().time().strftime('%H:%M:%S')}")
    print('-------------------------------')

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choices(chars, k=length))

Menu_str = """
---- Hello, I'am XolineAI ---- 

1. /date - today's date
2. /time - time now
3. /password - random password
4. /exit - exit the program

------------------------------
"""

print(Menu_str)

while True:

    menu_input = input("Enter your choice: ")

    if menu_input == "/date" or menu_input == '1':
        get_date()

    elif menu_input == "/time" or menu_input == '2':
        get_time()

    elif menu_input == "/password" or menu_input == '3':
        try:
            lenght_random = int(input("Enter password length: "))
            print(f"Your password: {generate_password(lenght_random)}")
        except ValueError:
            print("Please enter a valid value")

    elif menu_input == "/exit" or menu_input == '4':
        break

    else:
        print("Please enter a valid input")