row = int(input("enter row number : "))
col = int(input("enter column number : "))
multilist = [[0 for c in range(col)] for r in range(row)]

for r in range(row) :
    for c in range(col) :
        multilist[r][c] = r*c
print(multilist)
