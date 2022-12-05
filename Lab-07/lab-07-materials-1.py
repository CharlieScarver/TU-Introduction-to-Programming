# In a try statement with an except clause
# that mentions a particular class, that
# clause also handles any exception classes
# derived from that class

# Number cast - invalid value
valid = "5"
valid_float = "3.14"
invalid = "3@"
try:
    num = int(valid)
    print('Cast #1 =>', num)
    num = float(valid_float)
    print('Cast #2 =>', num)
    num = int(invalid)
    print('Cast #3 =>', num)
except ValueError as e:
    print('Invalid value - can\'t cast to number')
    print('ValueError message = {str(e)}')
    print(type(e))
else:
    print(f'num**2 = {num**2}')

# Module not found
try:
    a = 5
    import asd
    b = 4
except ModuleNotFoundError:
    print('Module not found')
else:
    asd.foo()

# Module not found
try:
    a = 5
    import asd
    b = 4
except ModuleNotFoundError:
    print('Module not found')
else:
    asd.foo()

# Undeclared name
try:
    print(a)
    print(b) # NameError
except NameError as e:
    print(f'Name error: {str(e)}')

# File not found
try:
    f = open('./asd', 'r')
except FileNotFoundError:
    print('File not found')
else:
    f.close()

# Callstack example
def f():
    a = 1
    b = 2
    c = a + b + 4
    print("c is", c)

    def g(n):
        for i in range(2, n):
            if n % i == 0:
                return False

        print("n is", n)
        p = n / 0
        print(p)
        return True

    y = 10
    try:
        is_p = g(c)
    except ZeroDivisionError as e:
        print("Division by zero!")
    else:
        if is_p:
            print(f"{c} is p")

    z = 1
    print(z)
        
f()

# Write to file, plain, no try-except
fruits = ["Orange\n", "Banana\n", "Apple\n"]
f = open("./file.txt", "w")
f.writelines(fruits)
# input('pause')
f.close()

# Write to file, with
with open("./file.txt", "w") as f:
    f.writelines(fruits)
    # 6 / 0


# Custom Exceptions
class MyException(Exception):
    def __init__(self, message="Custom error", *args):
        super().__init__(message, *args)

class CustomException(Exception):
    pass

class CustomException(Exception):
    pass

class InvalidParameter(Exception):
    pass

class InvalidAgeError(InvalidParameter):
    pass

class InvalidParameter(Exception):
    def __init__(self, invalid_parameter):
        message = f"Invalid class parameter: {invalid_parameter}"
        super().__init__(message)

try:
    raise InvalidParameter("name")
except InvalidParameter as e:
    print("Caught a custom exception:", str(e))

try:
    raise CustomException("Raised a customer exception")
except CustomException as e:
    print("Caught a custom exception:", str(e))
    
raise MyException()


###
# Add custom exceptions and try-except to the Animals homework task


