#Create a Tuple
my_tuple = ("apple", "banana", "cherry")
#Tuple constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Tuple items have a defined ordered, and the order will not change.
#Tuples cannot have items added or removed after it has been created.

#Tuples can allow duplicates because they are indexed.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Add a comma at the end of a one item tuple to define its type
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
#thistuple = ("apple")
#print(type(thistuple)) 

#Tuples can be any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#Tuples can contain mixed data types
tuple1 = ("abc", 34, True, 40, "male")

#The data type of a tuple is "tuple"
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

