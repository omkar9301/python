h  = int(input("input dog age in human  years : "))
if h < 0 :
    print("age must be possitive number")
elif h <= 2 :
    d = h*10.5
else :
    d = 21 + (h-2)*4
print("the dogs age in dog's years is : ",d)