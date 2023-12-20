from operation import Operation

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
