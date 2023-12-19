class ATM:
    def init(self, cash_available):
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
