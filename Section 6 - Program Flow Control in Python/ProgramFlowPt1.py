# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.

# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered.
# Examples of the input you may get are:
# 127. 0.0.1
# .192.168.0.1
# 10.0.123456.255
# 172.16
# 255

# So your program should work even with invalid IP Addresses. We're just interested in the
# number os segments and how long each one is.

# Once you have a working program, here are some more suggestions for invalid input to test:
# .123.45.678.91
# 123.4567.8.9.
# 123.156.289.19123456
# 10.10t.10.10
# 12.9.34.6.12.90
# '' - that is, press ented without typing anything

# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

ip = input("Write an IP address...\n")
print("===============")
sequence = ""
sequences = 0
sequenceSize = 0
ipLen = len(ip) - 1

for i in range(len(ip)):
	if ip[i] == ".":
		if sequence == "":
			print(sequence + " => " + str(sequenceSize))
			continue
		else:
			sequences += 1
			print(sequence + " => " + str(sequenceSize))
			sequence = ""
			sequenceSize = 0
	else:
		sequence += ip[i]
		sequenceSize += 1

print(sequence + " => " + str(sequenceSize))
sequence = ""
sequenceSize = 0
