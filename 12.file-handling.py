# Example 1: Writing to a file
with open('example.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('This is a file write example.\n')

# Example 2: Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print('File content:')
    print(content)

# Example 3: Reading line by line
with open('example.txt', 'r') as f:
    for line in f:
        print('Line:', line.strip())

# Example 4: Appending to a file
with open('example.txt', 'a') as f:
    f.write('Appending a new line.\n')

# Example 5: Using 'with' ensures file is closed automatically
def write_and_read(filename, text):
    with open(filename, 'w') as f:
        f.write(text)
    with open(filename, 'r') as f:
        return f.read()

result = write_and_read('sample.txt', 'Python file read/write demo.')
print(result)

import os
os.remove("demofile.txt")