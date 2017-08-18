# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

from random import randint

numbers = []

for i in range(0, 10, 1):
	numbers.append(randint(1, 50))

iterator = iter(numbers)

for number in numbers:
	print(next(iterator))
