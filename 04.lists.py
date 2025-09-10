# creating a list
list = ["apple","orange", "banana", "cherry"]
print(list)

# List length
print(len(list))

# Access list item
list1 = ["abc", 34, True, 40, "male"]
print(list1[1])

# Add list item
list.append("mango")
print(list)
list.insert(1, "litchi")
print(list)

# Remove list item
list.remove("banana")
print(list)
list.pop(1)
print(list)

# Extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Loop through a list
for x in list:
    print(x)

# Loop through a list
for i in range(len(list)):
    print(list[i])

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
