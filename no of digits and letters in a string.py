a = input("Enter a String : ")
d = 0
l = 0
for i in a :
    if i.isdigit() :
        d = d+1
    elif i.isalpha() :
        l = l+1
    else :
        pass
print("total no of digits : ",d)
print("total no of letters : ",l)
