x = 0
y = 1
a = int(input("enter number : ")) 
while y < a :
    print(y)
    x,y = y,x+y






i = 0
x = 0
y = 1
           
n = int(input("enter number : "))
while(i < n):
    if(i<=1):
        count = i
    else :
        count = x + y
        x = y
        y = count
    print(count)
    i = i + 1