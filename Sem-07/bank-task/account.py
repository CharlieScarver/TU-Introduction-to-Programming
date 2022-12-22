from errors import InvalidAccountType

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT")

    def __init__(self, iban, currency, type) -> None:
        if type not in Account.ACC_TYPES:
            raise InvalidAccountType()

        self.iban = iban
        self.currency = currency
        self.type = type
