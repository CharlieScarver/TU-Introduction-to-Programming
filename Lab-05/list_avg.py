def list_avg(lst, mult = 1):
    nsum = 0
    count = 0

    for i in lst:
        if type(i) == int or type(i) == float:
            nsum += i * mult
            count += 1
            print("int/float", i)
        elif type(i) == str and i.isnumeric():
            nsum += float(i) * mult
            count += 1
            print("str", i)

    if count == 0:
        print("Error: Division by zero")
        return

    print(nsum, count)
    return nsum / count


print(list_avg(['4', 1.5, "@7$", 3.5, (1, "hi")]))
# 3

print(list_avg(['6', 3, 3.0], 2))
# 8

print(list_avg(['%$', {}]))
# Error: Division by zero
# None

print(list_avg([]))
# Error: Division by zero
# None
