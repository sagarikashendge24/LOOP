n=int(input("ENTER THE NUMBER"))
x=0
y=1
z=1
while z<=n:
    # print(z)
    x=y
    y=z
    z=x+y  
print(z)    