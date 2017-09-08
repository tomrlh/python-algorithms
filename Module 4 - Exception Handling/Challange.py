# Our Program Will have two parts
# 1 => Age
# 2 => dividend and divisor

# We will cover following topics here
# 1 => Exception handling
# 2 => Try/Catch
# 3 => Try/else/finally
# 4 => Custom Exception

# Select one option
# 1 => Age
# 2 => Math

class CustomException(Exception):
	def __init__(self):
		self.default_message = "Option must be 1 or 2"

	def __str__(self):
		return self.default_message


class UserAgeException(CustomException):
	def __init__(self):
		self.default_message = "User age must be greater than - or less than 100"


class DivisorException(CustomException):
	def __init__(self):
		self.default_message = "Divisor must not be 0!"

def math_functionality():
	while 1:
		try:
			dividend = int(input("Please enter a dividend: "))
			divisor = int(input("Please enter a divisor: "))
			print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
			break
		except NameError:
			print("Dividend and Divisor myst be numbers!")
			continue
		except ZeroDivisionError:
			print("the dividend may not be zero!")
			
def age_functionality():
	try:
		use_age_input = int(input("Input a valid age:"))
	except NameError as e:
		print("\nAge must be a number!")
	if(user_age_input <= 0 or user_age_input >= 100):
		raise UserAgeException

def our_program():
	print('''
	Our program will have two parts:
	1 => Age
	2 => Dividend and divisor

	We will cover the following topics:
	1. Exception handling
	2. try/catch
	3. try/else/finally
	4. Custom Exception
	''')

	if(__name__ == "__main__"):
		our_program()
		print("Select one option\n1 => Age\n2 => Math")
		while 1:
			try:
				try:
					option_selected = int(input("Option:"))
				except NameError as e:
					print("\nOption must be an integer value")
					continue
				if(option_selected == 1):
					age_functionality()
				elif(option_selected == 2):
					math_functionality()
				if(option_selected <= 0 or option_selected >= 3):
					raise CustomException
			except ValueError as e:
				print("\nPlease select option between 1 & 2")
			except (CustomException, UserAgeException) as e:
				print("\nCustom exception occured: %s" % e)
			else:
				print("\nOptions executed successfully")
				break
			finally:
				print("\nThis is the finally block, it will always print at the end\n")