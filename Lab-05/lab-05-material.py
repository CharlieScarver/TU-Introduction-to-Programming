# What type is this?

a = 5,
b = {}
c = range(10)
d = [a]
e = [x for x in c]


##########

# Functions

# print(), input(), int(), list(), type()
# len(), round(), max(), sum(), random.choice()
# any(), all()

def my_func():
    print("print from my func")

my_func()

############

def greeting(name):
    print(f"Hi, I'm {name}")

greeting("Alex")
print("########")

############

import math

def is_prime(num):
    if num < 2:
        print(f"{num} is neither prime nor composite")
        return
    elif num % 2 == 0:
        print(f"{num} is composite")
        return
    
    end = math.ceil(math.sqrt(num)) + 1 # end is exclusive
    for i in range(3, end, 2):
        if num % i == 0:
            print(f"{num} is composite")
            break
    else:
        print(f"{num} is prime")

is_prime(0)
is_prime(1)
is_prime(2)
is_prime(3)
is_prime(30)
is_prime(51)
is_prime(-51)
is_prime(121)
is_prime(7919)
print("########")

############

def is_prime_bool(num):
    if num < 2:
        return False
    elif num % 2 == 0:
        return False
    
    end = math.ceil(math.sqrt(num)) + 1 # end is exclusive
    for i in range(3, end, 2):
        if num % i == 0:
            return False
    else:
        return True


def primes_in_interval(start, end): # end is inclusive
    for i in range(start, end+1):
        if is_prime_bool(i):
            print(f"{i} is prime")

primes_in_interval(25, 50)
print("########")

###########
# In Python we have objects and names referencing them
# Every objects stores a count - the number of references

# Sequence Types
#       - x in s, s + t, s * n
#       - s[i], s[i:j:k], len(s), max(s), s.index(x), s.count(x)

## Immutable Sequence Types
#       - lists, sets, dictionaries
#       - s[i] = x, del s[i:j], s[i:j:k] = t
#       - s.append() s.copy(), s.clear(), s.insert(i, x), s.pop(), s.remove()
#       - can be changed in functions, can't be reassigned

## Mutable Sequence Types
#       - strings, tuples, ranges
#       - hash()

###########

# Argument passing, references and rebinding

# Recall that in Python, every piece of data is an object.
# A reference points to an object, not a specific memory location.

x = 5
x = 10

# These assignment statements have the following meaning:

# The first statement causes x to point to an object whose value is 5.

# The next statement reassigns x as a new reference to a different
# object whose value is 10. Stated another way, the second assignment
# rebinds x to a different object with value 10.

# In Python, when you pass an argument to a function, a similar
# rebinding occurs. Consider this example:

def f(fx):
    fx = 10

x = 5
f(x)
print(x)    # 5

# Namespaces
# Local > Enclosing > Global (Module) > Built-in

dir()
dir(__builtins__)
globals()
locals()

# Variable scope
print("Variable scope:")

x = 'global'

def f():
    x = 'local'

f()
print(x)    # global

# Namespace resolution
# Local > Enclosing > Global > Built-in
print("Namespace resolution:")

###

name = "Alex"

def foo():
    print(f"{name}")

foo()


###

def foo():
    name = "Alex"

    def bar():
        print(f"{name}")

    bar()

foo()

###

x = 'global'

def f():
    x = 'enclosing'

    def g():
        x = 'local'
        print(x) # local

    g()
    print(x) # enclosing

f()
print(x)    # global

#
# Modifying global names in a function
print("Modifying global:")

x = 'global'

def f():
    global x
    x = 'local'

f()
print(x)    # local

#
# Modifying enclosing names in a function
print("Modifying enclosing:")

x = 'global'

def f():
    x = 'enclosing'

    def g():
        nonlocal x
        x = 'local'
        print(x) # local

    g()
    print(x) # local

f()
print(x)    # global

############

# Pass by value vs pass by reference
print("Modify function arguments:")

# Number
num = 5

def modify_num(num):
    print(num, id(num))
    num += 2
    print(num, id(num))

print(num, id(num))
modify_num(num)
print(num, id(num))

# String

s = "Hello"
def modify_str(s):
    s.lower()
    print(s, id(s))
    s = s.lower()
    print(s, id(s))

print(s, id(s))
modify_str(s)
print(s, id(s))

# List

lst = [43, 2, 17, 95]

def modify_list(lst):
    lst.sort()
    print(lst, id(lst))
    lst = [43, 2, 17, 95]
    print(lst, id(lst))

print(lst, id(lst))
modify_list(lst)
print(lst, id(lst))


# Reference count

import sys

print(sys.getrefcount(s)) #-- Returns the reference count of the object.

import gc

print("referrers count: ", len(gc.get_referrers(s)))
# for i in gc.get_referrers(s):
#    print(i)
