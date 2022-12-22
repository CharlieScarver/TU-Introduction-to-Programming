
file = open("data.csv", "r")

#print(file.read())
#print(file.readlines())
#print(file.readline())

for line in file:
    print(line)

file.close()
