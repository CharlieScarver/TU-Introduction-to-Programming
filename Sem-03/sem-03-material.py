# 0. Quick recap:

# Operators
a = 37
b = 5
c = a * b
c = a / b
c = a // b
print("37 div 5 = ", c)
c = a % b
print("37 mod 5 = ", c)
c = "Hello" + " " + "World"
c = "Hello" * 3
print(c)
c = 5 & 4           # 4
c = 6 || 5          # 7
c = 1 << 3          # 8
c = 37 & (1 << 5)   # 0
print(c)
c = True
c = False
c = 37 % 2 == 0
c = 37 >= 15
c = 37 < 100 and a == b     # False
c = 37 < 100 or a == b      # True
c = not 37 < 100            # False
c = 37 < 100 and not a == b # True

# Slicing operator [::]
s = "0123456"[1:3:1]     # 12
print(s)
s = "0123456"[:5:2]      # 024
print(s)
s = "0123456"[2:]        # 23456
print(s)
s = "0123456"[2:-2]      # 234
print(s)
s = "0123456"[:-2]      # 01234
print(s)
# Negative step means go from <end> to <start> instead (in reverse)
s = "0123456"[::-1]      # 6543210
print(s)
s = "0123456"[1::-1]      # 10
print(s)

# String formatting - 3 ways
name = "Alex"
s = "Hello, %s!" % (name)
s = "Hello, {}!".format(name)
s = f"Hello, {name}!"
print(s)

# print() and end="" parameter
print(1)
print(3)
print("asd")
print(1, end=" ")
print(3, end=" ")
print("asd", end=" ")


# if-elif-else statement
n = int(input('Enter number: '))
if n > 50:
    print('n > 50')
elif n < 50:
    print('n < 50')
else:
    print('n = 50')

# for loop
for i in range(1, 11):      # range(start=0, end, step=1)
 print(i)

for letter in range(ord('a'), ord('z')+1):
 print(chr(letter))

word = 'Python'
for letter in word:
 print(letter)

# while loop
n = 1
while n < 11:
    print(n)
    n += 1

# while True + break operator
n = int(input('enter number: '))
dsum = 0
while True:
    dsum += n % 10   # sum = sum + n
    n = n // 10
    if not n:       # if n == 0
        break
print(dsum)

# continue operator
for number in range(1, 20):
    if number == 5:
        continue
    if number == 11:
        break
    print(number)


# range(start=0, end, step=1)
# Negative step = iterate in reverse
for x in range(20, 10, -2):
    print(x, end=' ')

 

### Sem-03 ###

# Exercises from Lab-03 file
# +
# 0. Draw a mirrored triangle (n = 5, (n*2)-1 rows, max width = n)
# 1. Sum the digits of a given number
# 2. Write a program to display all prime numbers within a range (start, end)
# 3. Find the factorial of a given number
# 4: Reverse a given integer number
# 5. Display Fibonacci series up to a given number of terms
# 6. Use a loop to display elements from a given list
#    present at odd index positions
# 7. Find the sum of the series upto n terms (n = 5, 5+55+555+5555+55555)






