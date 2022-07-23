#Access List Items
thislist = ["apple", "banana", "cherry", "mango", "kiwi", "orange"]
print(thislist[1])  #banana
print(thislist[2:5]) #3rd 4th 5th item
print(thislist[:4]) #Leaving out 0 the range starts at first item
print(thislist[2:]) #All items from cherry to end

#Negative
print(thislist[-1]) #last item of list
print(thislist[-4:-1]) #cherry to kiwi

#Is an item in the list?
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 

#Add List Item
#Append a value at the end
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert a value at specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Remove List Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove By Index with pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Pop without index removes last item.
thislist.pop()

#Remove by Index with del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Del can also delete whole list
del thislist 

#Remove all items in list with clear
thislist.clear()
#Replace List Items

#Replace one value
thislist[1] = "blackcurrant"
print(thislist)

#Replace two values
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Replace one value with two values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

#Replace two values with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) 

#Joining lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

#Join with append
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 

#Extend a list with another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Extend a list with any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Copy a List with copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Copy a List with list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Copy list with comprehension
mylist = [x for x in fruits] 

#Sort a list ascending alphanumerically (case sensitive)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort a list ascending alphanumerically (case insensitive)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Sort Descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Reverse list with no sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Custom Sort
def myfunc(n):
  return abs(n - 50) #Closest to 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) 

#newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"] 

#Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

#While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

#Print indexes

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 

