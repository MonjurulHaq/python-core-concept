# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

thistuple = ("apple", "banana", "mango")
print(thistuple)
print(type(thistuple))

# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

tuple1 = ("abc", 34, True, 40, "male", 1)
print(tuple1)

# The tuple constractor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Access tuple items
# -1 refers to the last item, -2 refers to the second last item etc.
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])      # Returns the third, fourth, and fifth item:

# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


#Unpacking Tuples
# Assign the rest of the values as a list called "red" *:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Loop Through a Tuple
for i in range(len(thistuple)):
    print(thistuple[i])
    
# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
