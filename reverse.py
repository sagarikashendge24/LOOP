n=int(input("ENTER THE NUMBER"))
rev=0
while n>0:
    reminder=n%10
    rev=(rev*10)+reminder
    n=n//10
print(rev)
