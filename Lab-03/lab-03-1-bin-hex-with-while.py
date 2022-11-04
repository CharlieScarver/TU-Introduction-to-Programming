num = 27102022
devisor = 2

digits = "0123456789ABCDEF"
result = ""

# hex

while num > 0:
    remainder = num % 16

    digit = digits[remainder]

    result += digit
    
    num //= 16


print(result[::-1])
