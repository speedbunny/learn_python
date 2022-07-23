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
