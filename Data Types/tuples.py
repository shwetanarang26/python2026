empty_tuple = ()
person = ("john", 25, "New York")

numbers = 1, 2, 3, 4, 5, 6

print(person[0])
print(person[1])
print(person[-1])

# numbers[0] = 10
# To add or modify tuples
new_numbers = numbers + (7, 8)
print(new_numbers)
# tuples packing and unpacking
cordinates = 10, 20, 30
x, y,z = cordinates

print(x)
print(y)

#tuples methods
tuple_count = 1, 2, 2, 2, 3, 3, 5
print(tuple_count.count(2))
print(tuple_count.count(5))

def get_name_and_age():
    name = "Alice"
    age = 26
    return name, age
result = get_name_and_age()
print(result)