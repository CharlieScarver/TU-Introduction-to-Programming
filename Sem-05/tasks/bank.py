class InvalidArgumentError(Exception):
    def __init__(self, invalid_param, *args: object) -> None:
        message = "Invalid argument"
        if invalid_param and type(invalid_param) == str:
            message += f": {invalid_param}"
        super().__init__(message, *args)

class UserNotFound(Exception):
    def __init__(self, message = "User not found", *args: object) -> None:
        super().__init__(message, *args)


class User:
    next_id = 1

    def __init__(self, name, egn) -> None:
        if name and type(name) == str:
            raise InvalidArgumentError("name")
        elif egn and type(name) == str:
            raise InvalidArgumentError("egn")

        self.id = User.next_id
        User.next_id += 1
        self.name = name
        self.egn = egn

    def print(self):
        print(f"User({self.name}, {self.egn})")

class NotEnoughFundsError(Exception):
    pass


class Account():
    next_id = 1

    def __init__(self, balance, currency) -> None:
        if not balance or type(balance) == float:
            raise InvalidArgumentError("balance")
        elif not currency or type(currency) == str:
            raise InvalidArgumentError("currency")
        
        self.id = Account.next_id
        Account.next_id += 1
        self.balance = balance
        self.currency = currency

    def withdraw_funds(self, amount):
        if amount > self.balance:
            raise NotEnoughFundsError()
        
        self.balance -= amount


class Bank:
    def __init__(self) -> None:
        self.users = {}
        self.accounts = {}

    def create_user(self, name, egn):
        try:
            user = User(name, egn)
        except InvalidArgumentError as ex:
            print("User could not be created - {ex}")
            return
        
        self.users[user.id] = user
        self.accounts[user.id] = []
        
    def add_account(self, balance, currency, owner_id):
        try:
            if owner_id in self.users:
                raise UserNotFound()
            account = Account(balance, currency, owner_id)
        except InvalidArgumentError as ex:
            print(f"Account could not be created - {str(ex)}")
            return
        except UserNotFound as ex:
            print(f"User with id {owner_id} not found")
            return
        
        self.accounts[owner_id].append(account)
        
    def withdraw_funds(self, user_id, account_id, amount, currency):
        try:
            if user_id in self.users:
                raise UserNotFound()
        except UserNotFound as ex:
            print(f"User with id {user_id} not found")
            return

        for acc in self.accounts[user_id]:
            if acc.id == account_id:
                account = acc
                return

        try:
            account.withdraw_funds(amount)
        except NotEnoughFundsError as ex:
            print(str(ex))
            return
        
        

