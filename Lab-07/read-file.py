try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("Error: File not found")
else:
    print(f.read())
    f.close()