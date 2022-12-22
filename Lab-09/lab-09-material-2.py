class Student:
    def __init__(self, names, fac_num, pob, grade) -> None:
        self.names = names
        self.fac_num = fac_num
        self.pob = pob
        self.grade = grade
    
    def print(self):
        print(f"Student({self.names}, {self.grade})")

students = []

try:
    rfile = open("data.csv", "r")
    wfile = open("storage.csv", "w")
except OSError as ex:
    print(f"Error opening the file: {str(ex)}")
else:
    for line in rfile:
        print(line)

        line_split = line[:len(line)-1].split(",")
        students.append(Student(line_split[0], line_split[1], line_split[2], line_split[3]))

        new_line = line.replace("a", "-")
        wfile.write(new_line)

    rfile.close()
    wfile.close()


for s in students:
    s.print()