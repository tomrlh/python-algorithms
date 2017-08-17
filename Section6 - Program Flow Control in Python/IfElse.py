# Write a small program to ask for a name and an age.
# When botk values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Write your name...\n")
age = int(input("Write your age...\n"))

if age >= 18 and age < 31:
	print("Welcome to club 18-30 holidays, {0}\n" . format(name))
else:
	print("You haven't the required age to enter in the holiday\n")