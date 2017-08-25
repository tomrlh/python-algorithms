fruit = {
	"orange": "a sweet, orange, citrus fruit",
	"apple": "good for makind cider",
	"lemon": "a sour, yellow citrus fruit",
	"grape": "a small, sweet fruit growing in bunches",
	"lime": "a sour, green citrus fruit"
}

print(fruit["lemon"])

while True:
	idx = input("enter a fruit: ")
	print(fruit[idx])