from datetime import datetime

class Client:
    def __init__(self, name, account_number, pin, initial_balance=0):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def change_pin(self, new_pin):
        self.pin = new_pin

class ATM:
    def __init__(self, cash_available):
        self.cash_available = cash_available

    def check_balance(self, client):
        return client.get_balance()

    def withdraw_cash(self, client, amount):
        if amount > 0 and amount <= self.cash_available:
            if client.withdraw(amount):
                self.cash_available -= amount
                return True
        return False

    def update_cash(self, amount):
        if amount > 0:
            self.cash_available += amount

class Bank:
    def __init__(self):
        self.clients = []
        self.atms = []
        self.operations = []

    def add_client(self, client):
        self.clients.append(client)

    def add_atm(self, atm):
        self.atms.append(atm)

    def find_client_by_account_number(self, account_number):
        for client in self.clients:
            if client.account_number == account_number:
                return client
        return None

    def verify_pin(self, client, pin):
        return client.pin == pin

    def transfer_money(self, sender, receiver_account_number, amount):
        receiver = self.find_client_by_account_number(receiver_account_number)
        if receiver and sender.balance >= amount:
            sender.withdraw(amount)
            receiver.deposit(amount)
            self.operations.append(Operation(sender, "Transfer", amount))
            self.operations.append(Operation(receiver, "Deposit", amount))
            return True
        return False

class Operation:
    def __init__(self, client, operation_type, amount):
        self.client = client
        self.operation_type = operation_type
        self.amount = amount
        self.date_time = datetime.now()

bank = Bank()

client1 = Client("John Doe", "123456789", "1234", initial_balance=500)
client2 = Client("Jane Smith", "987654321", "5678", initial_balance=1000)

atm1 = ATM(5000)
atm2 = ATM(3000)

bank.add_client(client1)
bank.add_client(client2)

bank.add_atm(atm1)
bank.add_atm(atm2)

print("Client 1 balance:", bank.atms[0].check_balance(client1))

if bank.verify_pin(client1, "1234") and bank.atms[0].withdraw_cash(client1, 200):
    print("Withdrawal successful. Remaining balance:", client1.get_balance())
    print("ATM 1 cash available:", bank.atms[0].cash_available)
else:
    print("Withdrawal failed.")

if bank.transfer_money(client1, "987654321", 100):
    print("Transfer successful.")
    print("Client 1 balance:", client1.get_balance())
    print("Client 2 balance:", client2.get_balance())
    print("ATM 1 cash available:", bank.atms[0].cash_available)
else:
    print("Transfer failed.")
