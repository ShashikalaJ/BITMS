'''try:
    num=10
    deno=0
    
    result=num/deno
    
    print(result)
except:
    print("error:denominator cannot be 0.")

balaji=5/0
print(balaji)

try:
    
    even_numbers=[2,4,6,8]
    print(even_numbers[5])
    
except ZeroDivisionError:
    print("denominator cannot be 0.")
    
except IndexError:
    print("index out of bound")'''
    
    
try:
    num=int(input("enter a number:"))
    assert num % 2 == 0
    
except:
    print("not an even number")
    
else:
    reciprocal=1/num
    print(reciprocal)
            

    num=10
    deno
    