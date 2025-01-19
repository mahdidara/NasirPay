# NasirPay
# AmirMahdiDara
from os import system

clearcommand = "clear" # if you are useing mac or linux: 'clear' / if you are useing windows: 'cls'

users_list = []
account_number_list = [] # this list added for search easy with account numbers
usernames_list = []

def print_menu(menu , inp , result , is_numeric = False):
    system(clearcommand)
    print("Result: ")
    print(result)
    print("-"*40)
    print(menu)
    if is_numeric:
        while True:
            try:
                i = int(input(inp))
                return i
            except:
                print("You must enter a number. Please try again.")
    i = input(inp)
    return i

def get_correct_value(inp  , l = [] , is_numeric = False):
    '''
    baray check kardane in ke 
    age karbar meghdare khali dad 
    ya mighdar ghire adadi 
    ya yek chiz tekrari vared kard 
    dobare az karbar vorodi begirim
    '''
    while True:
        i = input(inp)
        if i == "":
            print("You cannot give an empty value.")
            continue
        if not i.isnumeric() and is_numeric:
            print("You must enter a number. Please try again.")
            continue
        if i in l:
            print(f"'{i}' is a duplicate. Please try again.")
            continue
        return i
            

class User:
    account_number = ""
    username = ""
    password = ""
    name = ""
    budget = 0
    def __init__(self , name , username , password , account_number , budget):
        self.name = name
        self.username = username
        self.password = password
        self.account_number = account_number
        self.budget = int(budget)
        users_list.append(self)
        account_number_list.append(self.account_number)
        usernames_list.append(self.username)
    def show_info(self):
        return f"Name: {self.name}\nAccount number: {self.account_number}\nBudget: {self.budget}"
    def check_budget(self):
        self.budget -= 1000
        return f"budget: {self.budget}"
    def fund_transfer(self , acc , num):
        try:
            index = account_number_list.index(acc)
        except:
            return False
        users_list[index].budget += num
        self.budget -= num
        return True

while True:
    system(clearcommand)
    print("  .:.Welcome to NasirPay.:.\n")
    print("(Login page)")
    u = input("Enter your username: ")
    p = input("Enter your password: ")
    if u == 'admin' and p == 'kntu':
        system(clearcommand)
        result = ""
        while True:
            print("Admin\n")
            menu = "1. Add a user\n2. remove a user\n3. Edit a user\n4. Search a user(by account number or by name)\n5. Deposit to a user\n6. Withdraw from a user\n7. Fund transfer\n8. Reporting all information\n9. Total bank balance\n10. changing a user's password\n11. Logout"
            inp = "Enter a number (1 , 5): "
            inp = print_menu(menu , inp , result , is_numeric=True)
            if inp == "1":
                print("  .:.Adding a user.:.")
                name = get_correct_value("Enter a name: ")
                username = get_correct_value("Enter a username: " , usernames_list)
                password = get_correct_value("Enter a password: " , is_numeric = True)
                account_number = get_correct_value("Enter an account number: " , account_number_list , is_numeric = True)
                budget = int(get_correct_value("Enter a number for budget: " , is_numeric=True))
                User(name , username , password , account_number , budget)

            elif inp == "2":
                pass
            elif inp == "3":
                pass
            elif inp == "4":
                pass
            elif inp == "5":
                pass
            elif inp == "6":
                pass
            elif inp == "7":
                pass
            elif inp == "8":
                pass
            elif inp == "9":
                pass
            elif inp == "10":
                pass
            elif inp == "11":
                pass
            else:
                result = f"'{inp}' is not defined!!!"
    else:
        pass
