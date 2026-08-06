
'''marks = int(input("Enter the marks (1-100):"))
if marks >0 and marks <=100:
        if marks >=90:
            print("user has secured grade A")
        if marks>=80 and marks<=89:
            print("user has secured grade B")
        if marks>=70 and marks<=79:
            print("user has secured grade C")
        if marks>=60 and marks<=69:
            print("user has secured grade D")
        if marks<60:
            print("User Failed")
else:
    print("Enter only +ve marks value greater than 0 and less than 100")
    '''
#elif keyword --> if -else -else
'''
if<condition>:
statement(s)...
elif <cond 1>...
   statement...
  elif<cond2>...
  statement ...
  ...
else:
    statement(s)...

marks=int(input("Enter the student marks:"))
if marks<0 and marks>100:
     print("Enter values should be greater than 1 and less than 100")
elif marks >=90 and marks <= 100:
    print("grade A")
elif marks >=80 and marks <=89:
    print("grade B")
elif marks >=70 and marks <=79:
    print("grade C")
elif marks >=60 and marks <=69:
    print("grade D")
elif marks<60 and marks>=0:
    print("user has failed")
else:
    ("print negative marks")
'''
#Voter eligibility checkcase
#<=18 and 100-->access
#<18 not eligible
# negative values-->not accetable
'''
age=int(input("Enter the age:"))
if age>=18 and age <=100:
    print("user has voter eligibility")
    print("Access granted")
elif age<18 and age>0:
    print(" user age is not eligible")
    print('user need to wait for more time',(18-age),'years')
else:
    print("only +ve values and less than 100 acceptable")
 '''

#Output -->print()    
#Output fromatting --> old stlye formating (using commas)
#% usage (%f,%d),.format() usage,fstring notation
'''
a,b= 7,9
print(a)
print(b)
print(a,b)
name = "Codegnan";batch = "Data analysis"
print(name,batch)#by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep=' ----->')
#end='\n','\t --->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("hyderabad")


name ='codegnan';age=7;batch='DA-23';place='HYD'
#usage of commas
print(batch,'is in',name)#variables and msg to be separated by commas
'''
#.format() usage
print("{} is in {}".format(name,place))#order matters
#fstring usage (more recommanded)
