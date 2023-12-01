from client import Client
class ATM:
    def __init__(self, cash_balance):
        self.cash_balance = cash_balance
    def withdraw_cash(self, clients, amounts, pins):
        if clients.get_pin() == pins:
            if(self.cash_balance >= amounts and clients.get_balance() >= amounts):
                clients.withdraw(amounts)
                self.cash_balance -= amounts
                print(f"Залишок готівки в банкоматі: {self.cash_balance}")
            else:
                print("Недостатньо коштів або немає коштів у банкоматі")
        else:
            print("Невірний PIN")
    def deposit_cash(self, clients, amounts, pins):
        if clients.get_pin() == pins:
            clients.deposit(amounts)
            self.cash_balance += amounts
            print(f"Поповнення {amounts} готівки успішно. Залишок готівки в банкоматі: {self.cash_balance}")
        else:
            print("Невірний PIN")
    def update_cash_balance(self, amount):
        self.cash_balance += amount
        print(f"Оновлено залишок готівки в банкоматі. Новий баланс: {self.cash_balance}")
    def get_cash(self):
        return self.cash_balance
    

