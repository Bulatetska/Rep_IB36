from atm import Atm
from bank import Bank
from client import Client
from operation import Operation

bank = Bank()

client1 = Client("John Doe", "123456789", "1454", initial_balance=500)
client2 = Client("Jane Smith", "987654321", "5578", initial_balance=1000)

atm1 = Atm(5000)
atm2 = Atm(3000)

bank.add_client(client1)
bank.add_client(client2)

bank.add_atm(atm1)
bank.add_atm(atm2)

print("Client 1 balance:", bank.atms[0].check_balance(client1))

if bank.verify_pin(client1, "1234") and bank.atms[0].withdraw_cash(client1, 200):
    print("Withdrawal was successful. Remaining balance:", client1.get_balance())
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