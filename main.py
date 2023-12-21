temp = input("enter temperature in cel : ")
degree = int(temp[:-1])
i = temp[-1]
if i.upper() == 'C' :
    result = int(round(9*degree)/5+32)
    o = "far"
elif i.upper() == 'F' :
    result = int(round(degree - 32) * 5 / 9)
    o = "cel"
else:
    print("wrong conversion")
    quit()
print("The temperature in", o, "is", result, "degrees.")

