tuple1 = 1, "two", 3, "four"
tuple2 = tuple1
tuple1 = 1, "two", 3, "four", 5
print("tuple1 = ", type(tuple1))
print("tuple2 = ", type(tuple2))

list1 = [1, 2, 3, 4]
list2 = 1, 2, 3, 4
list3 = 1
list4 = [1, "two", 3, "four"]
print("list1 = ", type(list1))
print("list2 = ", type(list2))
print("list3 = ", type(list3))
print("list4 = ", type(list4))