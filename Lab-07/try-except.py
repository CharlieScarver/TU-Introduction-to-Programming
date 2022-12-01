# Function documentation
""" int factoriel(int x):
Returns the factoriel of the given number x
Raises a ValueError if x is negative
"""
def factoriel(x):
    if x < 0:
        raise ValueError()

    if x == 0:
        return 1
    
    fact = 1
    for i in range(2, x+1):
        fact *= i

    return fact

try:
    print(factoriel(5))
    print(factoriel(-1))
except ValueError as ex:
    print(type(ex), "Invalid number")




def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)



filename = 'asd.txt' #input("Enter file name: ")

try:
    # ....
    f = open(f"./{filename}", "r")
except ZeroDivisionError:
    print("division by zero")
except (FileNotFoundError, OSError) as ex:
    #print("The file does not exist")
    print("Couldn't open the file")
    print(type(ex), str(ex))
#except :
    #print("OS couldn't open the file")
else:
    lines = f.readlines()
    f.close()
finally:
    print("Always executed")



try:
    5 / 0
except ZeroDivisionError:
    print("division by zero")

try:
    print(x)
except NameError:
    print("name error")


x = 'aSADasd'
try:
    f = float(x)
except ValueError:
    print("Invalid value")