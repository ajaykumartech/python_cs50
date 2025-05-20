# Create a tuple
my_tuple = (10, "Hello", 3.14, True, "Python")

# Print the tuple
print("The tuple is:", my_tuple)
print("Type of my_tuple:", type(my_tuple))

my_tuple = ("apple", "banana", "cherry", "date", "elderberry")

# Accessing elements
first_element = my_tuple[0]
last_element = my_tuple[-1]  # Negative indexing for the last element
third_element = my_tuple[2]  # Indexing starts from 0

print("Original tuple:", my_tuple)
print("First element:", first_element)
print("Last element:", last_element)
print("Third element:", third_element)




my_tuple = ("a", "b", "c", "d", "b", "e")
element_to_find = "b"

try:
    index = my_tuple.index(element_to_find)
    print("Tuple:", my_tuple)
    print(f"The first occurrence of '{element_to_find}' is at index: {index}")
except ValueError:
    print(f"'{element_to_find}' not found in the tuple.")

# To find all occurrences (more advanced, using a loop):
print("\nFinding all occurrences:")
indices = []
for i, item in enumerate(my_tuple):
    if item == element_to_find:
        indices.append(i)
if indices:
    print(f"'{element_to_find}' found at indices: {indices}")
else:
    print(f"'{element_to_find}' not found.")