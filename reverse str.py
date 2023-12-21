a = input("Enter a string : ")
print(a)
def reverse(a) :
    str = ""
    for i in a :
        str = i + str
    return str 
print(reverse(a))