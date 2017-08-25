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
			