def try_catch_finally():
	print("1st try/except")
	try:
		a = 6 + 'abc'
	except Exception as e:
		print(type(e))
		print(e)

	print("2nd try/except")
	try:
		a = 1/0
	except Exception as e:
		print(type(e))
		print(e)
	except ZeroDivisionError:
		print("ZerodivisionError")
	finally:
		print("inside finally")

	print("3rd try/except")
	try:
		a = 1 + abc
	except NameError as ne:
		print("inside NameError exception")
		print(ne)
	except Exception as e:
		print(type(e))
		print(e)
		print("inside generic exception")

	print("4th try/except")
	try:
		a = 1 + 'abc'
	except TypeError:
		print("type error")
	except Exception as e:
		print(type(e))
		print("Inside generic exception")



# raising exceptions
class AnException(RuntimeError):
	def __init__(self, arg):
		self.args = (arg,)


def raise_exception():
	try:
		raise Exception("an exception has been raised")
	except Exception as e:
		print(type(e))
		print(e)
		print("Inside exception raised")

	try:
		raise SystemError("a system error has been raised")
	except Exception as e:
		print(type(e))
		print(e)
		print("inside system error has been raised")

	try:
		raise AnException("a AnException has been raised")
	except SystemError as ne:
		print("inside System Error")
	except AnException as ae:
		print(type(ae))
		print(ae)
		print("inside AnException raised")
	except Exception as e:
		print("inside generic exception")


#try_catch_finally()
raise_exception()