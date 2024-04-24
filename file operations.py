fp=open("abc.txt",'w')
fp.write("hello")
print(fp)
if fp:
    print("done")
print(fp.closed)
fp.close()
#append
fp1=open("abc.txt",'a')
fp1.write("\nhow are you??")
fp1.writelines("todayits thursday the date is 18th of april")
print(fp1)
if fp1:
    print("done")
print(fp1.name)
fp1.close()
#read
fp2=open("abc.txt",'r')
print(fp2.read(15))
fp2.seek(0)
print(fp2.readline(2))
print(fp2.mode)
fp2.close()








