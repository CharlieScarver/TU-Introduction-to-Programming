### Quick Recap ###

# break statement
for val in "string":
    if val == "i":
        break
    print(val)

print("End")

# continue statement
for val in "string":
    if val == "i":
        continue
    print(val)

print("End")


# break example
num = 37
found_divisors = False
for i in range(2, num-1):
	if num % i == 0:
		found_divisors = True
		print(f"{num} is composite")
		break

if not found_divisors:
	print(f"{num} is prime")


# for-else
num = 14
for i in range(2, num-1):
	if num % i == 0:
		print(f"{num} is composite")
		break
else:
	print(f"{num} is prime")


### Collections

## The big four:
# 1. List
# Ordered, changeable, indexed, allows duplicate members
lst = list()
lst = []
lst = [1, "Hello", 3.14, 1]
a = lst[2]
lst.append(37)
lst.insert(2, 100)
lst.remove(3.14)  	# remove first value encountered
del lst[3] 			# delete element at index
lst = lst[2::2]
lst = lst[::-1]
l2 = lst.copy()
b = 1 in lst
print(f"\nList: {lst}, Length: {len(lst)}")
for el in lst:
	print(el)

# 2. Tuple
# Ordered, UNchangeable, indexed, allows duplicate members
tup = tuple()
tup = ()
tup = (1, "Hello", 3.14, 1)
a = tup[2]
tup = tup[2::2]
tup = tup[::-1]
b = 1 in tup
print(f"\nTuple: {tup}, Length: {len(tup)}")
for el in tup:
	print(el)

# 3. Set
# Unordered, UNchangeable*, UNindexed, doesn't allows duplicate members (removes them)
# A methematical logic set of unique values
s = set()
s = {1, "Hello", 3.14, 1}
s = {1, 3, 5, 7}
s2 = {1, 7}
s3 = {1, 2, 3, 4}
print()
print("s2 <= s: ", s2 <= s)		# is A a subset of B
print("s >= s2: ", s >= s2)		# is B a superset of A
print("s <= s3: ", s <= s3)		# is B a subset of A
print("s & s3: ", s & s3)		# intersection
print("s | s3: ", s | s3)		# union
print("s - s3: ", s - s3)		# difference A
print("s3 - s: ", s3 - s)		# difference B
print("s ^ s3: ", s ^ s3)		# symmetric difference
ss = s.copy()
ss.add(9)
ss.remove(7)
b = 1 in ss
print(f"\nSet: {ss}, Length: {len(ss)}")
for el in ss:
	print(el)

# 4. Dict
# Ordered (3.7+), changeable, Keyed, doesn't allow duplicate members
# Key-value mapping collection
# Implemented using a hash table in CPython
d = dict()
d = {}
d = {"a": 1, "b": 2, 37: 1.1, (1,2,3): "tuple key"}
a = d[(1,2,3)]
d = dict(name="Alex", age=22, heigh=187.2, job="Programmer")
a = d["name"]
del d["heigh"]
b = "name" in d
print(f"\nDict: {d}, Length: {len(d)}")
for key in d:
	print(key, d[key])

## Others:
# String
# Ordered, UNchangeable, indexed, allows duplicate members
st = str()
st = ""
st = "Hello World"
a = st[2] 
st = st[2::2]
st = st[::-1]
print(f"\nStr: {st}, Length: {len(st)}")

# Range
# Represents an immutable sequence of numbers. Indexed.
# Only works with an integer step and iterates one-way - either forward or in reverse.
r = range(0, 10, 1)
r = range(10)
temp = r[2]			# 2
r = r[1:9:2] 		# range(1, 9, 2) 
print("\nRange:", r)
for i in r:
	print(i)

# Exercise: What type is this?

a = 5,
b = {}
c = range(10)
d = [a]
e = [x*2 for x in c]
f = {1,}
g = set(list((None,)))
print("g: ", g, type(g))


### Functions
print("\n\nFunctions:")

# Function definition - positional arguments, default value
def factorial(n, multiplier=1):
	res = 1

	for i in range(2, n+1):
		res *= i

	return res * multiplier

#
print("factorial(5) = ", factorial(5))
print("factorial(n=5) = ", factorial(n=5))
print("factorial(5, 2) = ", factorial(5, 2))

# Variable-length argument tuple *args
def num_list(*items):
	lst = []
	for i in items:
		if type(i) == int:
			lst.append(i)

	return lst

#
print("num_list(1, 2.3, \"3\", 4, [1, 2], (1, 2)) = ", num_list(1, 2.3, "3", 4, [1, 2], (1, 2)))


# In Python we have objects (every piece of data) and names referencing them
# A reference points to an object, not a specific memory location
# Every objects stores a count - the number of references to it

x = 5
def change_num(x):
    x = 10

change_num(x)
print("\nchange_num(x) = ", x)

#

lst = [1, 2, 3]
def change_list(lst):
    lst.append(10)
    lst = [3, 4, 5]

change_list(lst)
print("change_list(lst) = ", lst)


# Namespace resolution
# Local > Enclosing > Global (Module) > Built-in

dir()
dir(__builtins__)
globals()
locals()

#
x = 'global'

def f():
    x = 'enclosing'

    def g():
        x = 'local'
        print(x) # local

    g()
    print(x) # enclosing

f()
print(x)    # global


### Collections Tasks:
# 1) Въвежда се число n. Трябва да покажете първите n+2 на брой числа на Фибоначи
# 2) Въвежда се число n. Трябва да принтирате колко е n факториел (n!).
# 3) Въвежда се число n. След това се въвеждат n на брой числа, които трябва да се запазят в списък. След това се въвежда още едно число, което може да е само 0 или 1. В зависимост от това какво е последното число:
#         - ако е 0 - към числата на четните индекси от списъка се прибавя 5
#         - ако е 1 - към числата на нечетните индекси от списъка се прибавя 10 
# След промените принтирате списъка от числа
#
# 4) Въвежда се число n. Трябва да принтирате следния израз на екрана (за n = 5):
#  5+55+555+5555+55555 = 61725
# За n = 3 трябва да е:
# 3+33+333 = 369
# Принтирайте  целия израз, не само резултата 
#
# 5) Имате два готови сета (множества) в програмата, няма да се въвеждат. 
# Ако първият е подмножество на втория, програмата трябва да принтира нов сет, който е разликата на втория с първия сет.
# Ако първият не е подмножество на втория, програмата трябва да принтира нов сет, който е обединението на двата сета.
# Пример 1:
# s1 = {2, 3}
# s2 = {1, 2, 3, 4}
# Изход:
# {1, 4}
# 
# Пример 2:
# s1 = {1, 7, 5}
# s2 = {1, 2, 3, 4}
# Изход:
# {1, 2, 3, 4, 5, 7}
# 
# 6) Въвежда се число n. След това се въвеждат n двойки от стойности, които ще са първо ключ и после стойност, към която ключа ще сочи. Трябва да направите речник (dict) и да сложите ключовете и стойностите в него. 
# След това се въвежда още едно число m. След него се въвеждат m на брой стойности, които трябва да запазите в списък.
# Ако някой от тези стойности е съществуващ ключ в речника, трябва на нейно място в списъка да сложите стойността към която сочи ключа на речника и да изтриете този ключ от речника.
# Накрая програмата ви трябва да принтира речника и списъка след извършените промени.
# Пример:
# 5
# name
# Ivan
# last_name
# Ivanov
# age
# 27
# height
# 181
# job
# Programmer
# 4
# last_name
# random
# age
# job
# 
# Изход:
# {'name': 'Ivan', 'height': 181}
# ['Apostolov', 'random', 27, 'Programmer']
# 

### Functions Tasks:
# 1) Разширени версии на функциите, които написах в клас:
# Функция input_nums(n), която приема параметър цяло число и иска от потребителя да въведе n на брой елемента, които връща (с return) в списък.
# Ако въведен елемент може да бъде преобразуван в цяло число (.isnumeric()) го преобразуваме и го добавяме на края на списъка, който връща функцията.
# Ако въведен елемент не може да бъде преобразуван в цяло число, той бива игнориран и не се добавя в резултатния списък.
# Ако параметърът на функцията n не е цяло число, функцията не иска от потребителя да въвежда елементи и директно връща празен списък.
# Пример:
# input_nums(3)
# # Enter a list element: 2
# # Enter a list element: G
# # Enter a list element: 3
# # [2, 3]
# 
# input_nums('a')
# # []
# 
# Функция sum_list(lst), която приема параметър списък и връща сумата на елементите му.
# В сумата влизат само елементи, които са числа (цели и дробни) и такива, които могат да се преобразуват в числа (като "5") като първо се преобразуват и после се добавят към сумата.
# Елементи, които не са числа (цели и дробни) и не могат да се конвертират към такива, се игнорират и не влияят на сумата.
# Ако списъкът се състои само от невалидни елементи се очаква функцията да върне сума 0.
# Пример:
#  sum_list([1, "a", 3.14, "5"])
# # 9.14
# 
# sum_list(["asd", "-"])
# # 0 
# Една допълнителна функция max_of_two(a, b), която приема две числа a и б и връща по-голямото от тях.
# Ако числата са равни, връща винаги първото (а).
# Ако единият от параметрите не е число, връща другия.
# Ако и двата параметъра не са числа, не връща нищо (празен return).
# Пример:
# max_of_two(2.5, 13)
# # 13
# 
# max_of_two("@#$", {})
# # 
# 
# max_of_two('a', 5)
# # 5
# 
# След като всички функции са готови трябва да можете да напишете без грешка следните изрази (и да можете да ги обясните):
# max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3)))
# # ???
# 
# max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
# # ??? 
# 
# 2) Напишете функция list_avg(lst, multiplier) която намира средното аритметичната стойност от подаден списък с елементи.
# В списъка може да има и елементи, които не са числа. Те трябва да се пропускат от калкулацията (не влизат нито в сумата нито в бройката)
# Функцията има втори параметър multiplier, който не е задължителен.
# Ако е подаден, функцията трябва да провери дали е цяло число и ако не е да принтира грешка и да прекрати изпълнението си.
# Ако multiplier е подаден и е цяло число, трябва всеки елемент на списъка, който може да бъде умножен по него, ако е възможно. Това умножение се извършва преди сметката за средното аритметично. Тоест средното ще бъде сметнато от умножените елементи.
# Пример: 
# Ако не е подаден, се приема че е равен на 1 и функцията просто връща средното аритметично без да прави умножение.
# 
# 3) Напишете функция digitize(num), която приема цяло число и връща tuple, в който се съдържат цифрите на числото като отделни елементи (като числови стойности, не като стрингове).
# Функцията трябва да валидира дали подаденият параметър е цяло число и да принтира грешка и да спре изпълнението си,  ако не е.
# Използвайте разпадането на tuple на отделни променливи, за да предадете резултата на функцията на няколко променливи (всяка е равна на една цифра) и ги принтирайте.
# a, b, c, d = digitize(1337) 
# 
# 4) Говорихме, че може да се дефинира функция вътре в друга функция. 
# Напишете функция get_collection_builder(col_type) която връща друга функция спрямо подадения стринг параметър col_type.
# Функцията трябва да валидира дали параметърът е стринг.
# Ако col_type е “tuple”, get_collection_builder връща функция, която приема 4 параметъра и връща tuple с тях.
# Ако col_type е “list”, се връща функция, която приема 4 праметъра и връща list с тях.
# Ако col_type е “set”, се връща функция, която приема 4 праметъра и връща set с тях.
# Върнатата функция трябва да е дефинирана вътре в get_collection_builder.
# Пример:
# tuple_builder = get_collection_builder(“tuple”)
# tup = tuple_builder(1, 2.23, 3, “hi”)
# # (1, 2.23, 3, “hi”)
#
# 5) Напишете функция is_valid_triangle(a, b, c), която да връща (True/False) дали може да съществува триъгълник с подадените три страни (цели числа, валидирайте ги).
# Говорихме как функциите са стойности и мога да се предават от едно място на друго и да има различни референции към една и съща функция. 
# Напишете код, който ще позволи следните две извиквания да извикват същата функция (все едно тя има две имена):
# is_valid_triangle(3, 4, 5)
# и
# can_triangle_exist(3, 4, 5)
# 