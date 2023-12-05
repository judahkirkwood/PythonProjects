animal = ( 'zebra', 'alligator', 'giraffe', 'goat', 'ox')
listofAnimals = list(animal)
print(listofAnimals)
listofAnimals.append ("honey badger")

myString = "Hello! I am pleased to meet you"
newString = list(myString)
print(newString)
newString = myString.split(" ")
print(newString)

myList = [2, 4, 6]
len(myList)
for i in myList:
    print(i)

myList.append(8)
print(myList)

myList2 = [1, 3, 7, 9]

myTuple = ("apple", "banana", "plum", "orange")
for i in myTuple:
    print(i)

count = myTuple2.count(3)
print("the element 3 appears", count, "times in the tuple.")

mySet = {"baseball", "basketball", "football"}
mySet.remove("basketball")
mySet.add("basketball")
mySet2 = {"baseball", "basketball", "football", "foosball"}
print(mySet)
