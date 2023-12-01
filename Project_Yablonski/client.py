class Client:
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def get_pin(self):
        return self.pin
    
    def withdraw(self, amount):
        
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Зняття {amount} успішно. Новий баланс: {self.balance}")
            return True
        else:
            print("Недостатньо коштів або недійсна сума зняття.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит на суму {amount} успішно внесено. Новий баланс: {self.balance}")
        else:
            print("Недійсна сума депозиту.")

    def change_pin(self, new_pin):
        if len(str(new_pin)) == 4:
            self.pin = new_pin
            print("PIN успішно змінено.")
        else:
            print("Недійсний PIN-код. Введіть 4-значний PIN-код.")

# Приклад використання класу:
# Створення об'єкта клієнта

