# User
class InvalidUserData(Exception):
    pass

class UserNotFound(Exception):
    pass

class UserAlreadyExists(Exception):
    def __init__(self, message = "User already exists", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyOwnsAccount(Exception):
    pass

# Account 
class AccountNotFound(Exception):
    pass

class UnsufficientBalance(Exception):
    pass

class InvalidAccountData(Exception):
    pass

class InvalidAccountType(Exception):
    pass

# Bank


# Menu
class InvalidMenuChoice(Exception):
    pass
