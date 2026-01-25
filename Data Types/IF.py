x, y = 5, 10
if x > y:
    print("x is greater")
elif (x + 10) < y:
    print("x is less")    
elif (x + 5) == y:
    print('equal')   


x, y, z = 5, 10, 5
if x > y:
    print("x is greater")
elif x <= y:
    if x == z:
         print("x is equal to z")    
elif x != z:
    print("x is not equal to z")   

x, y, z = 2, 4, 6
if x < y:
    print("x is less than y")
elif x < 6:
    print("x is greater")    
