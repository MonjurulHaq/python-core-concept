# In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")
my_function()

#Argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function2():
  pass

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)
my_function(x = 3)

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

#Recursion
def factorial(x):
  if x == 1:
    return x
  else:
    return x * factorial(x-1)

print(f"Factorial : {factorial(5)}")