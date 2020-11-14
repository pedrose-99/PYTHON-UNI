max_num = 100
min_num = 1

def read_number(max_num, min_num):
	correct = False
	while (not correct):
		try:
			number = int(input("Please, enter an integer number (1-100):"))
			if (number > min_num and number <= max_num):
				correct = True
		except ValueError:
			print("The number must be between 1-100")
	return number

def not_multiple(num, multiple):
	resto = num % multiple
	if resto != 0:
		return True
	else:
		return False

def print_list(list_prime):
	for num in list_prime:
		print(list_prime[num])

def search_prime(range_max):
	list_prime = []
	range_max = int(range_max)
	for num in range_max:
		if (not_multiple(num, 2) or not_multiple(num, 3) or not_multiple(num, 5) or not_multiple(num, 7) or not_multiple(num, 11)):
			list_prime.append(num)
	print("The prime numbers between 1 and ", range_max," are:", print_list(list_prime))
					

number = read_number(max_num, min_num)
search_prime(number)