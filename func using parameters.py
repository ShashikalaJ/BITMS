def balaji(a,b):
    print("my result bank balance=",a+b)

#initializing dictionary
#check for function name as key
test_dict = {"fname":balaji,"age":50,"address":"salem"}

#printing original dictionary
print("the original dictionary is:"+str(test_dict))

#calling function using brackets
res=test_dict['fname'](10,20)

#printing result
print("the required call result:"+str(res))