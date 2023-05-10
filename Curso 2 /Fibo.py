'''
crear una seria de finonacci con while 
hasta el numero 1597

'''


x = 0
y = 1
while y <= 1597 : 
    x = x + y 
    y = x + y
    print(x, y)

'''
x   y   x   y   x   y
0 + 1 = 1 + 2 = 3 + 4 = 7
'''