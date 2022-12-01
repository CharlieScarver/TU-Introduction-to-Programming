
# Task 2

def numeric(n):
    if type(n) != int:
        print("error")
        return

    if n == 1:
        # ... 5
        pass
    elif n == 0:
        # ... 10
        pass
    


def list_avg(lst, mult = 1):
    if type(lst) != list:
        print("List has to be of type list")
        return
    
    nsum = 0
    count = 0

    for i in lst:
        if type(i) == int or type(i) == float:
            nsum += i * mult
            count += 1
        elif type(i) == str and i.isnumeric():
            nsum += float(i) * mult
            count += 1

    if count == 0:
        print("Division by zero")
        return

    return nsum / count


l = [1, 2, "3", "@AA", (1, 2)]

druga = list_avg

def druga_f(lst, mult = 1):
    return list_avg(lst, mult)

print(druga(l))

print(list_avg(l))
print(list_avg(l, 2))


def function():
    pass


t = (1, 2, 3)


l2 = [x+2 for x in t]

l2 = []
for x in t:
    l2.append(x+2)



l = [1, 2, "3", "@AA", (1, 2), "37.1"]
l2 = [float(x) for x in l if type(x) == str and x.isnumeric()]

print(l2)

















            

