# NasirPay
# AmirMahdiDara
from os import system

clearcommand = "clear" # if you are useing mac or linux: 'clear' / if you are useing windows: 'cls'

users_list = []
account_number_list = [] # this list added for search easy with account numbers
usernames_list = []
loan_application = {}

def print_menu(menu , inp , result):
    system(clearcommand)
    print("Result: ")
    print(result)
    print("-"*40)
    print(menu)
    i = input(inp)
    return i

def get_correct_value(inp  , l = [] , is_numeric = False , find = False , max_lim = False , min_lim = False):
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
        if i in l and not find:
            print(f"'{i}' is a duplicate. Please try again.")
            continue
        if find:
            if i in l:
                return l.index(i)
            else:
                return False
        if not(max_lim is False):
            if int(i) > max_lim:
                print(f"Maximum is {max_lim}. Please try again.")
                continue
        if not(min_lim is False):
            if int(i) < min_lim:
                print(f"Minimum is {min_lim}. Please try again.")
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
        return f"Name: {self.name}\nAccount number: {self.account_number}\nBudget: {self.budget}\n"
    def check_budget(self):
        self.budget -= 1000
        return f"Budget: {self.budget}"

sw = False
while True:
    system(clearcommand)
    print("  .:.Welcome to NasirPay.:.\n")
    print("  (Login page)\n")
    if sw:
        print(" !!!The username or password is incorrect!!!\n")
    sw = False
    u = input("Enter your username: ")
    p = input("Enter your password: ")
    if u == 'admin' and p == 'kntu':
        system(clearcommand)
        result = ""
        while True:
            menu = "  Admin\n\n1. Add a user\n2. remove a user\n3. Edit a user\n4. Search a user(by account number or by name)\n5. Withdraw from a user\n6. Deposit to a user\n7. Fund transfer\n8. Reporting all information\n9. Total bank balance\n10. changing a user's password\n11. Show all load application\n12. Logout"
            inp = "Enter a number (1 , 12): "
            inp = print_menu(menu , inp , result)
            if inp == "1":
                system(clearcommand)
                print("  .:.Adding a user.:.\n")
                name = get_correct_value("Enter a name: ")
                username = "admin"
                s = False
                while username == 'admin':
                    if s:
                        print("The word admin is not acceptable. Please try again.")
                    username = get_correct_value("Enter a username: " , usernames_list)
                    s = True
                password = get_correct_value("Enter a password: " , is_numeric = True)
                account_number = get_correct_value("Enter an account number: " , account_number_list , is_numeric = True)
                budget = int(get_correct_value("Enter a number for budget: " , is_numeric=True , min_lim=100000))
                User(name , username , password , account_number , budget)
                result = f"{name} added."
            elif inp == "2":
                system(clearcommand)
                print("  .:.Deleting an account.:.\n")
                account_number_index = get_correct_value("Enter an account number: " , account_number_list , is_numeric=True , find=True)
                if account_number_index is not False:
                    users_list.pop(account_number_index)
                    account_number_list.pop(account_number_index)
                    usernames_list.pop(account_number_index)
                    result = "Deleted."
                else:
                    result = "This account number does not exist!!!"

            elif inp == "3":
                system(clearcommand)
                print("  .:.Editing an account.:.\n")
                account_number_index = get_correct_value("Enter an account number for edit: " , account_number_list , is_numeric=True , find=True)
                if account_number_index is not False:
                    usernames_list_copy = usernames_list.copy()
                    usernames_list_copy.pop(account_number_index)
                    account_number_list_copy = account_number_list.copy()
                    account_number_list_copy.pop(account_number_index)
                    user = users_list[account_number_index]
                    users_list[account_number_index].name = get_correct_value(f"Enter a name({user.name}): ")
                    users_list[account_number_index].username = get_correct_value(f"Enter a username({user.username}): " , usernames_list_copy)
                    usernames_list[account_number_index] = users_list[account_number_index].username
                    users_list[account_number_index].password = get_correct_value(f"Enter a password({user.password}): " , is_numeric = True)
                    users_list[account_number_index].account_number = get_correct_value(f"Enter an account number({user.account_number}): " , account_number_list_copy , is_numeric = True)
                    account_number_list[account_number_index] = users_list[account_number_index].account_number
                    users_list[account_number_index].budget = int(get_correct_value(f"Enter a number for budget({user.budget}): " , is_numeric=True , min_lim=100000))
                    result = "Done."
                else:
                    result = "This account number does not exist!!!"
            elif inp == "4":
                result = ""
                while True:
                    system(clearcommand)
                    print("  .:.Searching.:.\n")
                    menu = "1. Search by account number\n2. Search by name\n3. Back"
                    inp = "Enter a number: "
                    inp = print_menu(menu , inp , result)
                    result = ""
                    if inp == '1':
                        account_number_index = get_correct_value("Enter an account number: " , account_number_list , is_numeric=True , find=True)
                        if account_number_index is not False:
                            result = users_list[account_number_index].show_info()
                        else:
                            result = "This account number does not exist!!!"
                    elif inp == '2':
                        name = input("Enter a name: ")
                        result = ""
                        for i in users_list:
                            if name in i.name:
                                result += i.show_info() + "-"*20 + "\n"
                        if result == "":
                            result = f"'{name}' does not exist!!!"
                    elif inp == '3':
                        break
                    else:
                        result = f"'{inp}' is not defined!!!"
            elif inp == "5":
                system(clearcommand)
                print("  .:.Withdraw from a user.:.")
                account_number_index = get_correct_value("Enter an account number for Withdraw: " , account_number_list , is_numeric=True , find=True)
                if account_number_index is not False:
                    max_limit = users_list[account_number_index].budget - 100000
                    number = int(get_correct_value(f"Enter a number for Withdraw(max = {max_limit}): " , is_numeric=True , max_lim=max_limit))
                    users_list[account_number_index].budget -= number
                    result = "Done.\n" + users_list[account_number_index].show_info()
                else:
                    result = "This account number does not exist!!!"
            elif inp == "6":
                system(clearcommand)
                print("  .:.Deposit to a user.:.")
                account_number_index = get_correct_value("Enter an account number for Withdraw: " , account_number_list , is_numeric=True , find=True)
                if account_number_index is not False:
                    number = int(get_correct_value(f"Enter a number for Desposit(min = 0): " , is_numeric=True , min_lim=0))
                    users_list[account_number_index].budget += number
                    result = "Done.\n" + users_list[account_number_index].show_info()
                else:
                    result = "This account number does not exist!!!"
            elif inp == "7":
                system(clearcommand)
                print("  .:.Fund transfer.:.\n")
                account_number_index1 = get_correct_value("Enter the source account number: " , account_number_list , is_numeric=True , find=True)
                account_number_index2 = get_correct_value("Enter the destination account number: " , account_number_list , is_numeric=True , find=True)
                if (account_number_index1 is not False) and (account_number_index2 is not False):
                    max_limit = users_list[account_number_index1].budget - 100000
                    number = int(get_correct_value(f"Enter a number for Withdraw from '{users_list[account_number_index1].name}'(max = {max_limit}): " , is_numeric=True , max_lim=max_limit))
                    users_list[account_number_index1].budget -= number
                    users_list[account_number_index2].budget += number
                    result = "Done.\n" + users_list[account_number_index1].show_info() + "\n" + users_list[account_number_index2].show_info()
                else:
                    result = "One of the account numbers does not exist."
            elif inp == "8":
                system(clearcommand)
                print("  .:.All users.:.")
                result = ""
                for i in users_list:
                    result += i.show_info() + "-"*10 + "\n"
            elif inp == "9":
                system(clearcommand)
                total = 0
                for i in users_list:
                    total += i.budget
                result = f"Total: {total}"
            elif inp == "10":
                system(clearcommand)
                print("  .:.changing a user's password.:.\n")
                account_number_index = get_correct_value("Enter an account number for changing password: " , account_number_list , is_numeric=True , find=True)
                if account_number_index is not False:
                    new_pass = get_correct_value(f"Enter new password({users_list[account_number_index].password}): " , is_numeric=True)
                    users_list[account_number_index].password = new_pass
                    result = "Done."
                else:
                    result = "This account number does not exist!!!"
            elif inp == "11":
                result = ""
                for i , j in loan_application.items():
                    result += f"{i.name}: {j}\n"
                if result == "":
                    result = "There are no loan applications."
            elif inp == "12":
                break
            else:
                result = f"'{inp}' is not defined!!!"
    else:
        if u in usernames_list:
            username_index = usernames_list.index(u)
            if users_list[username_index].password == p:
                system(clearcommand)
                user = users_list[username_index]
                user_index = username_index
                result = ""
                while True:
                    menu = f"  {user.name}\n\n1. View account balance(-1000)\n2. Transfer funds to another account\n3. Loan application\n4. Change password\n5. Logout"
                    inp = "Enter a number (1 , 5): "
                    inp = print_menu(menu , inp , result)
                    if inp == '1':
                        result = user.check_budget()
                    elif inp == '2':
                        system(clearcommand)
                        print("  .:.Transfer funds to another account.:.")
                        account_number_index = get_correct_value("Enter an account number for transfer: " , account_number_list , is_numeric=True , find=True)
                        if account_number_index is not False:
                            max_limit = user.budget - 100000
                            number = int(get_correct_value(f"Enter a number for transfer(max = {max_limit}): " , is_numeric=True , max_lim=max_limit))
                            user.budget -= number
                            users_list[account_number_index].budget += number
                            result = "Done.\n" + f"Account balance: {user.budget}"
                        else:
                            result = "This account number does not exist!!!"
                    elif inp == '3':
                        system(clearcommand)
                        print("  .:.Loan application.:.\n")
                        load = input("Write your text for a loan application: ")
                        loan_application[user] = load
                        result = "Done."
                    elif inp == '4':
                        system(clearcommand)
                        print("  .:.Changing your password.:.\n")
                        new_pass = get_correct_value(f"Enter new password({user.password}): " , is_numeric=True)
                        user.password = new_pass
                        result = 'Done.'
                    elif inp == '5':
                        break
                    else:
                        result = f"'{inp}' is not defined!!!"

        else:
            sw = True
