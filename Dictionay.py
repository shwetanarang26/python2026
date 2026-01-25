person = {'name': 'John', 'age': '39', 'city': 'New york'}
print(person['name'])

person['email'] = 'john@example.com'

print(person)

del person['city']
print(person)

for key in person:
    print(key, person[key])
for value in person.values():
    print(value) 