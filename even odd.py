a = (1,2,3,4,5)
odd = 0
even = 0

for i in a :
    if not i % 2:
        even+=1
    else:
        odd+=1
print("even numbers : ",even)
print("odd numbers : ",odd)        