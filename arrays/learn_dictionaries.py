#Dictionary items are ordered(>3.7), changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#Create a dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Look up a dictionary value
print(thisdict["brand"])

#Values can be any data type
thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

#Dictionary datatype is "dict"
print(type(thisdict)) 
