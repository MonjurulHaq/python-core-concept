#Assign String to a Variable
a = "Hello"
# a = 'Hello'
print(a)

# Multiline Strings
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


# Quotes Inside Quotes
print("It's alright")
print("He is called 'Monjur'")
print('He is called "Monjur"')

# Slice From the Start
b = "Hello, World!"
print(b[:5])        # Hello

# Slice To the End
print(b[2:])        # llo, World!   

# Negative Indexing
print(b[-5:-2])     # orl

# Uppercase and Lowercase
print(b.upper())
print(b.lower())

# Remove Whitespace
print(b.strip())

# Replace String
print(b.replace("H", "J"))

# Split String
print(b.split(","))

# String Concatenation
print(a+" "+b)

# String Format
age = 36
print(f"My name is John, and I am {age}")

