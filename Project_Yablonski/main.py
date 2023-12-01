import client
from atm import ATM


atm1 = ATM(1000) #Банкомат
client_one = client.Client("John Doe", "123456789", "1234", 200) #обєкт клієнт

# Отримання балансу
print(f"Поточний баланас: {client_one.get_balance()}")

# пінкоду 
print(f"Поточний pin: {client_one.get_pin()}")

#Банкомат
# Зміна PIN-коду
#client1.change_pin("5678")

# Зняття коштів
atm1.withdraw_cash(client_one, 200, "1234")

# Внесення коштів
atm1.deposit_cash(client_one,200, "1234")

print(f"Поточний баланас: {client_one.get_balance()}")

# Оновлення кількості готівки в банкоматі
#atm1.update_cash_balance(0)