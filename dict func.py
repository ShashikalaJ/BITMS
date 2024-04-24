def balaji():
    return "this is my bank balance"

#initializing dictionary
#check for function name as key
test_dict = {"fname":balaji,"age":50,"address":"salem"}

#printing original dictionary
print("the original dictionary is:"+str(test_dict))

#calling function using brackets
res=test_dict['fname']()

#printing result
print("the required call result:"+str(res))