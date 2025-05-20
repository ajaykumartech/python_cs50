def divide_numbers(a, b):
    try:
        result = a / b
        print("Inside try block: Division successful.")
    except ZeroDivisionError as e:
        print(f"Error in except block: Cannot divide by zero! ({e})")
        result = None # Or some default value
    except TypeError as e:
        print(f"Error in except block: Invalid input types for division! ({e})")
        result = None
    else:
        print("Inside else block: No exceptions occurred.")
    finally:
        print("Inside finally block: This will always execute.")
    return result

print(divide_numbers(10, 2))
# print("-" * 20)
# print(divide_numbers(10, 0))
# print("-" * 20)
# print(divide_numbers(10, "a"))
# print("-" * 20)
# print(divide_numbers("b", 2))


def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:  # Use elif to check this only if age is not negative
        raise Exception("User must be 18 or older.") # Or a more specific custom exception
    # If neither of the above conditions is met, the age is valid
    print(f"Age {age} is valid.")

# --- Test Case 1: Negative Age ---
print("--- Test Case 1: Negative Age ---")
try:
    check_age(-5)
except ValueError as e:
    print(f"Caught ValueError: {e}")
except Exception as e: # Good practice to have a fallback for unexpected exceptions
    print(f"Caught unexpected Exception: {e}")

print("\n--- Test Case 2: Underage (Non-Negative) ---")
# --- Test Case 2: Underage (Non-Negative) ---
try:
    check_age(16)
except ValueError as e: # This won't be caught for age 16
    print(f"Caught ValueError: {e}")
except Exception as e:  # This will catch the "User must be 18 or older" exception
    print(f"Caught Exception: {e}")

print("\n--- Test Case 3: Valid Age ---")
# --- Test Case 3: Valid Age ---
try:
    check_age(25)
except ValueError as e:
    print(f"Caught ValueError: {e}")
except Exception as e:
    print(f"Caught Exception: {e}")

print("\n--- Test Case 4: Another Valid Age (Edge Case) ---")
# --- Test Case 4: Another Valid Age (Edge Case) ---
try:
    check_age(18)
except ValueError as e:
    print(f"Caught ValueError: {e}")
except Exception as e:
    print(f"Caught Exception: {e}")