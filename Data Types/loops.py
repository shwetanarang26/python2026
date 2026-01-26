for num in range(5):
    print("value: {}". format(num))

for num in range(2,10,2):
    print("value: {}".format(num))   

for num in range(5):
    if num == 3:
        continue
    print(num)     


for num in range(5):
    if num == 3:
        break
    print(num) 

health = 10
while health > 0:
    print(health)
    health -= 1

for i in range(2):
    for j in range(3):
        print(i,j)        

i = 1
while i < 10:
    print(i)
    i +=1
print(i)    


total = 0
number = 0
while number >= 0:
    total += number
    number = int(input("enter a number (negative to quit): "))
print("The sum is:" , total)     

