from errors import UserAlreadyOwnsAccount

class User:
    def __init__(self, names, egn) -> None:
        self.names = names
        self.egn = egn
        self.accounts = []

    def get_print(self):
        return f"User({self.names}, {self.egn}, accounts: [{len(self.accounts)}])"

    def add_account(self, account):
        if account in self.accounts:
            raise UserAlreadyOwnsAccount("Error: This account already belongs to this user")
            
        self.accounts.append(account)


