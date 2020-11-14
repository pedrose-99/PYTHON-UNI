min_n = 0
max_n = 10

class Student:
	def __init__(self, dni, p, score):
		self.dni = dni
		self.p = p
		self.score = score

	def __str__(self):
		cadena = ("DNI : " + str(self.dni) +" Nexp: "+ str(self.p) +" Score: "+ str(self.score))
		return cadena

def read_students(min_n):
	correct = False
	while not correct:
		try:
			number = int(input("Please, enter the number of students you want to add:"))
			if number > min_n:
				correct = True
		except ValueError:
			print("Incorrect value.", end=" ")
	return number

def read_nexp(min_n):
	correct = False
	while not correct:
		try:
			number = int(input("Please, enter nexp:"))
			if number > min_n:
				correct = True
		except ValueError:
			print("Incorrect value.", end=" ")
	return number  

def read_score(min_n, max_n):
	correct = False
	while not correct:
		try:
			number = float(input("Please, enter score:"))
			if min_n <= number <= max_n:
				correct = True
		except ValueError:
			print("Incorrect value.", end=" ")
	return number 

def read_dni():
	correct = False
	while not correct:
		dni = input("Enter the DNI:")
		if len(dni) == 9 and dni[0:7].isdigit() and dni[-1].isalpha():
			correct = True
	return dni

def max_score(list_students):
	score_max = 0
	pos = 0
	for std in list_students:
		if std.score > score_max:
			score_max = std.score
	while list_students[pos].score != score_max:
		pos = pos + 1
	return list_students[pos]

def min_score(list_students):
	score_min = 10
	pos = 0
	for std in list_students:
		if std.score < score_min:
			score_min = std.score
	while list_students[pos].score != score_min:
		pos = pos + 1
	return list_students[pos]

list_students = []
students = read_students(min_n)
while (len(list_students) < students):
	dni = read_dni()
	p = read_nexp(min_n)
	score = read_score(min_n, max_n)
	class_student = Student(dni, p, score)
	list_students.append(class_student)
higher_student = max_score(list_students)
lower_student = min_score(list_students)
print("Higher student: ", higher_student.__str__())
print("Lower student: ", lower_student.__str__())