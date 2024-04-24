date=int(input("enter the date:"))
if(date<=31):
    print("d=date")
else:
    print("incorrect date")
month=int(input("enter the month"))
if(month<=12):
    print("m=month")
else:
    print("incorrect month")
year=int(input("enter the year:"))
if(year>=1000 and year<=1999):
    print("y=year")
else:
    print("incorrect year")
c=year//100
d=year%100
month=month-2
f=date+((13*month-1)/5)+d+(d/4)+(c/4)-2*c

fres=int(f%7)
def days():
    day={0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}
print(days[fres])


