from datetime import datetime

class Operation:
    def __init__(self, client, operation_type, amount):
        self.client = client
        self.operation_type = operation_type
        self.amount = amount
        self.date_time = datetime.now()