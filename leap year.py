n=[2004,1996,10,17,85]
i=int(input("enter a number"))
if(n%4==0):
    print("leap year")
    if(n%i==0):
        print("prime")
    else:
        print("not prime")
    print("leap year")
else:
    print("not a leap year")