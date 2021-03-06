#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#If you add new items to a list, the new items will be placed at the end of the list.

#Create a List of Numbers
my_list = []
for x in range(1,10):
my_list.append(x)

#One-shot List
my_list = [x for x in range(1,10)]

#List constructor
my_list = list(("apple", "banana", "cherry"))

#Elements are referenced by numbers
first_ele = my_list[0]
last_ele = my_list[-1]

#Operators for statistics
how_many_items = len(my_list)
biggest_val = max(my_list)
smallest_val = min(my_list)
avg_val = sum(my_list) / len(my_list)

#List Datatypes
list1 = ["apple", "banana", "cherry"] #string
list2 = [1, 5, 7, 9, 3] #numeric
list3 = [True, False, False] #bool
list4 = ["abc", 34, True, 40, "male"] #mixed
print(type(my_list)) #What Datatype is it?


