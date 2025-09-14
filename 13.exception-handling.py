# 13.exception-handling

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("Execution completed.")

# Example usage
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, 'a')


# Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")


# Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")