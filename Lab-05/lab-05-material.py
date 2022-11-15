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

############
# Pass by value vs pass by reference

num = 5

def modify_num(num):
    num += 2

print(num)
modify_num(num)
print(num)

s = "Hello"
def modify_str(s):
    s.lower()

print(s)
modify_str(s)
print(s)

lst = [43, 2, 17, 95]

def modify_list(lst):
    lst.sort()
    lst = "new value"

print(lst)
modify_list(lst)
print(lst)


def foo():
    name = "Alex"

    def bar():
        print(f"{name}")

    bar()

foo()

# Reference count

import sys

print(sys.getrefcount(s)) #-- Returns the reference count of the object.

import gc

print(len(gc.get_referrers(s)))
for i in gc.get_referrers(s):
    print(i)

# In Python we have objects and names referencing them
# Every objects stores a count - the number of references


