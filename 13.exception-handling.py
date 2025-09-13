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