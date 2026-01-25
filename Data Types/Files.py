file = open('data.txt', 'w')
file.write('Hello\n')
file.write('World\n')
file.close()
file = open('data.txt', 'r')
content = file.read
print(content)