# Given the tuple below that represents the Imelda May album "more Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when print them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
	(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

tracks = imelda[3]
album, artist, year = imelda[0], imelda[1], imelda[2]
print(album)
print(artist)
print(year)

for track in tracks:
	print("Track number: " + str(track[0]) + ", Title: " + str(track[1]))