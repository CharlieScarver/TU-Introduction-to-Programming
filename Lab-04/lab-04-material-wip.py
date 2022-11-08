# Create list
s = [1, 3, 5, 7]
s = list((1, 2, 3, 4))
s = list("Python")
s = []
s.append(1)
s.append("a")
s.append(3.14)
print(s)
# Using a "list comprehension"
s = list(k for k in range(1,21) if k%3 != 0)
print(s)

# Get/set element by index
s = [2, 4, 6, 8]
print(s[0])
s[0] = 7
print(s[0])

# Slicing operator [::]
# [начало:край:стъпка]
s = [1, 2, 3, 4, 5, 6]
print(s[::-1]) # извеждаме елементите в обратен ред
print(s[:-1]) # принтираме без последния елемент
print(s[1:]) # принтираме без първия елемент
print(s[0:2]) # първите два елемента
print(s[-1:]) # последният елемент

# List concatenation
s = [1, 2, 3, 4, 5, 6]
s1 = [9, 8]
s2 = s +s1
print(s2)

# Iterate with for
s = [1, 2, 3, 4, 5, 6]
for i in s:
    print(i, end=' ') 
print()

# List comprehension print
[print(i) for i in s]

# Iterate with for with range() or enumerate()

# Check if element is contained
s = [2, 4, 6, 8]
print(4 in s) # True
