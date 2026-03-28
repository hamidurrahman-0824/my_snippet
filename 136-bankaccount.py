class BankAccount:
    total_customer = 0
    total_bank_balance = 0
    total_trans = 0 
    customer = {'abc':1001,'def':1002,'efg':1004}
    def __init__(self,name,id):
        self.balance = 0
        self.name = name
        self.id = id
        BankAccount.customer[id] = name
        BankAccount.total_customer += 1

    def add_money(self,amount):
        if amount>=1:
            
            self.balance += amount
            
            BankAccount.total_bank_balance += amount
            return f"{amount} added successfully."
        else:
            return f"Amount must be positive"
        
    def withdraw(self,amount):
        if self.balance>=amount:
            BankAccount.total_trans +=1
            BankAccount.total_bank_balance -= amount
            self.balance -= amount
            return f"{amount} withdrew successfully."
        else:
            return f"Insufficient fund."

    def send_money(self,amount,other):
        if amount>=1 and other.lower() in BankAccount.customer:
            BankAccount.total_trans +=1
            self.balance -= amount
            return f"Send money of {amount} to {other} successful"
        elif amount<1:
            return f"{amount} must be positive"
        else:
            return f"{other} do not exist in our bank."
    
    def show(self,id):
        if id in BankAccount.customer:
            return f"{BankAccount[id]},{id},{self.balance}"
    def __repr__(self):
        return f"(name={self.name}),(id={self.id}),balance={self.balance}"
    def stat(self):
        return f"Total customer={BankAccount.total_customer}\nTotal balance={BankAccount.total_bank_balance}\nTotal transection={BankAccount.total_trans}"
#improved
class BankAccount:
    total_customer = 0
    total_bank_balance = 0
    total_trans = 0

    customer = {1001:'abc',1002:'def',1004:'efg'}

    def __init__(self,name,id):
        self.balance = 0
        self.name = name
        self.id = id
        BankAccount.customer[id] = name
        BankAccount.total_customer += 1

    def add_money(self,amount):
        if amount >= 1:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            return f"{amount} added successfully."
        else:
            return "Amount must be positive"

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            BankAccount.total_trans += 1
            return f"{amount} withdrew successfully."
        else:
            return "Insufficient fund."

    def send_money(self,amount,other_id):
        if amount < 1:
            return "Amount must be positive"
        elif other_id not in BankAccount.customer:
            return f"{other_id} does not exist in our bank."
        elif self.balance < amount:
            return "Insufficient fund."
        else:
            self.balance -= amount
            BankAccount.total_trans += 1
            return f"Send money of {amount} to {BankAccount.customer[other_id]} successful"

    def show(self,id):
        if id in BankAccount.customer:
            return f"{BankAccount.customer[id]}, {id}, {self.balance}"

    def __repr__(self):
        return f"(name={self.name}), (id={self.id}), balance={self.balance}"

    def stat(self):
        return f"""Total customer = {BankAccount.total_customer}
Total balance = {BankAccount.total_bank_balance}
Total transaction = {BankAccount.total_trans}"""

#more improved
class BankAccount:
    
    accounts = {}                 # store all account objects
    total_customer = 0
    total_bank_balance = 0
    total_transaction = 0

    def __init__(self, name, acc_id):
        self.name = name
        self.id = acc_id
        self.balance = 0

        BankAccount.accounts[acc_id] = self
        BankAccount.total_customer += 1

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive."

        self.balance += amount
        BankAccount.total_bank_balance += amount
        return f"{amount} added successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive."

        if self.balance < amount:
            return "Insufficient balance."

        self.balance -= amount
        BankAccount.total_bank_balance -= amount
        BankAccount.total_transaction += 1
        return f"{amount} withdrawn successfully."

    def send_money(self, amount, receiver_id):

        if amount <= 0:
            return "Amount must be positive."

        if receiver_id not in BankAccount.accounts:
            return "Receiver account does not exist."

        if self.balance < amount:
            return "Insufficient balance."

        receiver = BankAccount.accounts[receiver_id]

        self.balance -= amount
        receiver.balance += amount

        BankAccount.total_transaction += 1

        return f"{amount} sent to {receiver.name} successfully."

    def show_balance(self):
        return f"{self.name} (ID:{self.id}) Balance = {self.balance}"

    def __repr__(self):
        return f"Account(name={self.name}, id={self.id}, balance={self.balance})"

    @classmethod
    def bank_statistics(cls):
        return f"""
Total Customers: {cls.total_customer}
Total Bank Balance: {cls.total_bank_balance}
Total Transactions: {cls.total_transaction}
"""