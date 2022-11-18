import random

lst = []
for i in range(9):
    lst.append(random.randint(0, 5))

# lst = random.sample(range(0, 8), 8)

print("Random list:", lst)

for i in range(0, len(lst)*2 - 2, 2): # 1 2 3
    lst.insert(i+1, lst[i] + lst[i+1]) # 1 3 2 3

print("Final list:", lst)
