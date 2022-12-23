try:
    rfile = open("data.txt", "r")
    wfile = open("storage.txt", "w")
except OSError as ex:
    print(f"Error: {str(ex)}")
else:
    for line in rfile:
        print(line.replace("\n", "").split(","))
        wfile.write(line.replace("a", ""))

    print("Cursor position", rfile.tell())
    rfile.seek(0)

    for line in rfile:
        print(line.replace("\n", "+"))

    rfile.close()
    wfile.close()

print()

with open("data.txt", "r") as rfile:
    while True:
        line = rfile.readline()

        if line == "":
            break

        print(line, end="")