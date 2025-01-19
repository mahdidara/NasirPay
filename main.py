# NasirPay
# AmirMahdiDara
from os import system

clearcommand = "clear" # if you are useing mac or linux: 'clear' / if you are useing windows: 'cls'

users_list = []
account_number_list = [] # this list added for search easy with account numbers

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
        self.budget = budget
        users_list.append(self)
        account_number_list.append(self.account_number)
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
    
