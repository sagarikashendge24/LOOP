user=int(input("ENTER THE NUMBER"))
i=2
a=0
while i<=user :
    if user%i==0:
        print(i)
        a=a+1
    i=i+1
    if a==2:
        print("IT IS PRIME NUMBER")
        break
    else:
        print("IT IS NOT PRIME NUMBER")        
