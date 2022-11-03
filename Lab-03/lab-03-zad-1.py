
num_count = int(input("How many numbers: "))

max_num = 0
i = 1

while i <= num_count:
    num = int(input(f"Enter number {i}: "))

    if num > max_num:
        max_num = num
    
    i += 1

print(f"Max number: {max_num}")


    
