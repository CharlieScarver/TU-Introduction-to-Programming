# Factorial of a number using recursion

def rfactorial(n):
   if n == 0 or n == 1:
       return 1
   else:
       return n*rfactorial(n-1)

print("0! = ", rfactorial(0))
print("3! = ", rfactorial(3))
print("5! = ", rfactorial(5))

