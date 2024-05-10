binary number
i=0
while i<=5:
    print(" 1 0"*i,"1",end="")
    j=0
    while j>i:
        print("1",end="")
        j-=1
    print()    
    i=i+1    