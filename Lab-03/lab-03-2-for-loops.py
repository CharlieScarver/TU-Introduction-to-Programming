# strings are sequences of characters
# sequences can be indexed using square brackets
# sequence[i] will give you the element at index i
digits = "0123456789ABCDEF"

# for loop that iterates the range 0-15
# and uses the current number to index the digits string
for i in range(15):
    print(i, digits[i])

# 0 0
# 1 1
# ...
# 10 A
# 11 B
# ...
# 15 F

# range works with start, end, step just like the slicing operator [::]
# range(start, end, step) - end is not inclusive
for i in range(2, 10, 2):
    print(i, digits[i])

# 2 2
# 4 4
# 6 6
# 8 8

# for can be used to iterate over any sequence
# here we iterate directly over digits:
for d in digits:
    print(d) # d is the current character from digits

# 0
# 1
# ...
# E
# F

# if we want not only the current index as well we can use enumerate:
for i, d in enumerate(digits):
    print(i, d)

# 0 0
# 1 1
# ...
# 15 F
