# Modify the program below to use a while loop top
# allow as many guesses as necessary.

# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.

# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

# #Original Code

# import random

# highest = 10
# answer = random.randint(1, highest)

# print("Please guess a number between 1 and {}: " . format(highest))
# guess = int(input())
# if guess != answer:
# 	if guess < answer:
# 		print("Please guess higher")
# 	else: # guess must be greater than number
# 		print("Please guess lower")
# 	guess = int(input())
# 	if guess = answer:
# 		print("Well done, you guessed it")
# 	else:
# 		print("Sorry, you have not guessed correcty")
# else:
# 	print("You got it first time")

# Trying Python
import random

highest = 10
answer = random.randint(1, highest)
print(answer)
print("Please guess a number between 1 and {}: " . format(highest))
guess = int(input())

while guess != answer:
	if guess < answer:
		print("Please guess higher")
		guess = int(input())
	elif guess > answer:
		print("Please guess lower")
		guess = int(input())

print("Well done, you guesses it")

