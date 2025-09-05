import random
import datetime

class BankAccount:
    promo_prize = 2000

    def __init__(self, name, balance, has_promo=False, sms=False, email=False, isAdmin = False):
        if has_promo:
            balance += self.promo_prize

        self.acc_name = name
        self.acc_number = random.randint(100, 1000)
        self.date_time = str(datetime.date.today())
        self.balance = balance
        self.sms = sms
        self.email = email
        self.isAdmin = isAdmin
        self.is_frozen = False

    def details(self):
            return f"Name: {self.acc_name}, Number: {self.acc_number}, Balance: {self.balance}"

    def deposit(self, amount):
        if self.is_frozen:
            return "Transaction Not Completed! Account is Frozen!"

        self.balance += amount
        return self.message("credit", amount)
        #return f"Credit Alert {self.acc_name}, New Balance: {self.balance}"

    def withdrawal(self, amount):
        if self.is_frozen:
            return "Transaction Not Completed! Account is Frozen!"

        if amount > self.balance: 
            return "Insuficient Funds!"

        elif amount < 0:
            return "Invalid Input for Amount!"

        else:
            self.balance -= amount
            return self.message("debit", amount)
            #return f"Debit Alert: Amount: {amount}, Acct Name: {self.acc_name}, New Balance: {self.balance}"

    def transfer(self, amount, to_acc):
        if self.is_frozen:
            return "Transaction Not Completed! Account is Frozen!"

        if amount > self.balance:
            return "Insuficient Funds!"
        
        elif amount < 0:
            return "Invalid Input for Amount!"

        else:
            #self.balance -= amount
            self.withdrawal(amount)
            sender_message = self.message("debit", amount)

            to_acc.deposit(amount)
            recievers_message = to_acc.message("credit", amount)

            return f"{sender_message} \n {recievers_message}"
            #return f"Transfer Successful! Amount: {amount}, Transfer to {to_acc.details()}"

    def message(self, transaction_type, amount):
        if transaction_type == "credit":
            transaction_alert = f"Credit Alert {self.acc_name}, New Balance: {self.balance} Time: {self.date_time}"

        elif transaction_type == "debit":
            transaction_alert = f"Debit Alert {self.acc_name}, New Balance: {self.balance} Time: {self.date_time}"

        else:
            transaction_alert = f"Transaction Alert: Acct: {self.acc_name}, New Balance: {self.balance} Time: {self.date_time}"


        if self.sms and self.email:
            return f"SMS: {transaction_alert} \n EMAIL: {transaction_alert}"

        elif self.sms:
            return f"SMS: {transaction_alert}"

        elif self.email:
            return f"EMAIL: {transaction_alert}"

        else:
            #return transaction_alert
            return None

    def account_freeze(self, acct):
        if self.isAdmin:
            acct.is_frozen = True
            return f"Your Account Has Been Frozen!"

        else:
            return f"You're Not An Admin to freeze the Account!"

    def account_unfreeze(self, acct):
        if self.isAdmin:
            acct.is_frozen = False
            return f"Your Account Has Been Unfrozen!"

        else:
            return f"You're Not An Admin! to Unfreeze"


admin = BankAccount("Dan", 5000, isAdmin=True)
john = BankAccount("John", 5000, has_promo=True, sms=True, email=True)
tom = BankAccount("Tom", 2000, has_promo=False, sms=True, email=False)

print(john.details())
print(tom.details())
print("")
print(john.deposit(1000))
print("")
print(john.withdrawal(500))
print("")
print(john.transfer(1500, tom))
print("")
print(john.account_freeze(admin))

(admin.account_freeze(john))

print("")
print(john.deposit(1000))
print(john.withdrawal(500))
print(john.transfer(1500, tom))

(admin.account_unfreeze(john))

print("")
print(john.deposit(1000))

print("")
print(tom.transfer(1500, admin))
print(tom.transfer(1500, john))

