# count how many times a word appears in the file and display the largest word.
# if have more than 1 word with the same size, it displays the fisrt one.

fileName = input("Please Enter File name(Press 0 to start with a default file):")

file_path = "/home/tomurlh/Documents/Projetos de Programação/Python/UdemyCoursePython/python-algorithms/Module 3 - Functions and Classes/default-file.txt"

words = {}
largestWord = ['word', 0]

print("File Data:")
print("----------------------------------------------------------")

with open(file_path, 'rt') as f:
	for line in f:
		print(line)
		wordsInLine = len(line.split())
		wordsSplited = line.split()

		for word in wordsSplited:
			if len(word) > largestWord[1]:
				largestWord[0] = word
				largestWord[1] = len(word)

			if word in words:
				newValue = words[word]
				words[word] = newValue + 1
			else:
				words[word] = 1

print("----------------------------------------------------------")
print("End File Data")
print("")
print("Repeating Elements:")
print("----------------------------------------------------------")
print(words)
print("----------------------------------------------------------")
print("End Repeating Elements")
print("")
print("Largest Element:")
print("----------------------------------------------------------")
print(largestWord[0])
print("----------------------------------------------------------")
print("End Largest Element:")