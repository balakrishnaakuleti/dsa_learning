class LowBalanceException(Exception):
    def __init__(self, msg:str) -> None:
        super().__init__(msg)
    
def withdraw_amount(amount,balance):
    if balance < amount:
        raise LowBalanceException("Insufficient funds")

