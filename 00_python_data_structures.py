# ()
fruits = ['apple', 'banana', 'cherry', 'apple']
print(f"List:  {fruits}")

fruits.append('orange')
fruits.insert(1, 'blueberry')
removed = fruits.pop(2)
fruits.remove('apple')
print(f"Modified list: {fruits}, removed: {removed}")

squares = [x**2 for x in range(1, 6)]
print(f"List comprehension: {squares}")

print(f"Sliced list: {fruits[1:3]}")
print(f"Reversed list: {fruits[::-1]}")

# tuples
coordinates = (10, 20, 30)
x, y, z = coordinates # unpacking
print(f"Tuple: {coordinates}, unpacked: x={x}, y={y}, z={z}")

single_item = ('hello',) # single item tuple needs a trailing comma
print(f"Single item tupple: {single_item}")

# dictionaries
person = {
	'name': 'Bob',
	'age': 25,
	'is_student': False
}
print(f"Dictionary: {person}")

print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

print(f"Salary and default value: {person.get('salary', 'Not specified')}")

squared_numbers = {x: x**2 for x in range(1, 6)}
print(f"Dict comprehension: {squared_numbers}")

# sets
unique_numbers = {1, 2, 3, 4, 3, 2, 1} # duplicating numbers
print(f"Set: {unique_numbers}") # no duplicates

set_a = {1,2,3,4,5}
set_b = {6,7,8,9,10}

print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference: {set_a - set_b}")
print(f"Symmetric difference: {set_a ^ set_b}")

unique_numbers.add(5)
unique_numbers.remove(3)  # Raises error if not found
unique_numbers.discard(10)  # Does not raise error if not found
print(f"Modified set: {unique_numbers}")

even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Set comprehension: {even_squares}")

# strings
text = "Python Programming"
print(f"String: {text}")

print(f"Uppercase: {text.upper()}")
print(f"Find 'gram': {text.find('gram')}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")

# collections
from collections import Counter, defaultdict, namedtuple

# Counter
word_counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(f"Counter: {word_counts}")
print(f"Most common: {word_counts.most_common(1)}")

# defaultdict
fruit_colors = defaultdict(list)
fruit_colors['red'].append('apple')
fruit_colors['yellow'].append('banana')
print(f"defaultdict: {dict(fruit_colors)}")

# namedtuple
Person = namedtuple('Person', ['name', 'age', 'job'])
bob = Person('Bob', 30, 'Engineer')
print(f"namedtuple: {bob}, Age: {bob.age}")

# arrays
numbers = [1, 2, 3, 4, 5]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flattening a matrix
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")

evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# Map and filter with functions
def square(x): return x**2

squares_func = list(map(square, numbers))
print(f"Map: {squares_func}")

evens_func = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter: {evens_func}")
