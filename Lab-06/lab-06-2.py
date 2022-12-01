
class Student:
    pass


name = "Alex"
fac_num = "121222414"
avg_grade = 5.5

name2 = "Alex"
fac_num2 = "121222414"
avg_grade2 = 5.5

name3 = "Alex"
fac_num3 = "121222414"
avg_grade3 = 5.5


name4 = "Alex"
fac_num4 = "121222414"
avg_grade4 = 5.5


class Student:
    def __init__(self, name, fac_num, avg_grade):
        self.name = name
        self.fac_num = fac_num
        self.avg_grade = avg_grade

    def say_hi(self):
        print(f"Hello, my name is {self.name}")
	
    def wrong_f():
        print("oops")

alex = Student("Alex", "121222404", 5.5)
ivan = Student("Ivan", "121222488", 5.1)
petar = Student("Petar", "121222123", 4.8)

students = []

students.append(alex)
students.append(ivan)
students.append(petar)

print(students)
