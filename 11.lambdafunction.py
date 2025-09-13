# Examples of lambda functions in Python

# Basic lambda function
add = lambda x, y: x + y
print("Sum:", add(5, 3))  # Output: 8

# Lambda with map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)  # Output: [1, 4, 9, 16]

# Lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: [2, 4]

# Lambda with sorted
pairs = [(2, 5), (1, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("Sorted by second element:", sorted_pairs)  # Output: [(4, 1), (1, 2), (2, 5)]

# Lambda in function arguments
def apply_func(f, value):
    return f(value)

result = apply_func(lambda x: x * 10, 7)
print("Applied lambda:", result)  # Output: 70