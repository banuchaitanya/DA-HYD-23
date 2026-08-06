'''
Identity Operators  --> checks the identity of the objects-->id()

a = [1,2,4,5]
b=a
print(id(a))
print(id(b))
c = [1,2,4,5]
#As we can lists mutable collection bothnc and a lists will have different values
print (c is a)#false
print (c==a)#output is True
print(c is not a)#Output is true



#Bitwise opertions --> we perform bitwise opertions over operands
# &(and),| (or), ^(XOR),shifting operators(<<,>>)
print(5&3) #both5 and 3 to be converted into binary and bitwise and is performed
print(5|3)#bitwise OR
print(5^3) #bitwise XOR

print(5<1)#false comparsion
print(5<<1)
print(15<<2)

#Input Formatting -->input(),int(input()),float(input())
#you know -->single input
#2 or 3 inputs -->map()
#group of intergers -->lists(map(int,input().split(','))

names = input("Enter the names:").split(',')
print(names)


syntax :
    if <condition>:
        statement(s)...

#age=15
age =int(input("Enter the age:"))
if age>=18 and age in[19,20,21]:
    print('Your age is:',age)
    

if <condition>:
    statement...
    ....
else:
    statement(s)..
    ...
'''
#vote eligibility -->To check voter eligibilty and give access
age=int(input("Enter the age:"))
if age>=18:
    print("You have voter eligibilty and age is",age)
    print("access granted")
else:
    age=18-age
    print("not eligible")
    


    
