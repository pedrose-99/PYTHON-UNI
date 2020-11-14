def geometric_average(numbers, total):
	return numbers ** ( 1 / total)

even_product = 1
counter = 0
finish = False

while not finish:
	try:
		user_input = input('Enter number from 1 to 999 (0 to finish): ')
		user_input = int(user_input)
		if user_input == 0:
			finish = True
		elif 0 < user_input <= 1000:
			if user_input % 2 == 0:
				even_product = even_product * int(user_input)
				counter = counter + 1   
		else:
			print('Value out of range! Please enter a positive even numbers less than 1000.', end=" ")
	except ValueError:
		print("That was not a number.", end=" ")

if counter > 0:
	num = geometric_average(even_product, counter)
	print('The geometric mean is: ', "{0:.3f}".format(num))
    
else:
	print('No positive even number less than 1000 was entered.')