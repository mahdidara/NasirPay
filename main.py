# NasirPay
# AmirMahdiDara

users_list = []
account_number_list = [] # this list added for search easy with account numbers

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
