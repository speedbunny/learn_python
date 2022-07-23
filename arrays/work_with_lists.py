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
#Change List Items

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
