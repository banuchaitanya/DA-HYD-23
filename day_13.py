'''
Tokens,Datatypes-->control flow stmts -->if,elif,else,for,while,break,continue

procedure oriented programming

functions--> A function is a block of code which performs a specific tasks
 Its a reusable group of statements where we define using def keyword
 Advantages--> Code usability,code maintainability,easy of debugging,avoiding code duplication...,modularity

def fname(parameters):
     """Doc String"""
     statements....
     .....
     return value(S).....
fname(args)
'''
#To perform sum of given objects
'''
def add(a,b):
    """Sum of objects"""
    c=a+b
    return c
print(add(12,3))#addition
print(add('code','gnan')) #Concatenation
print(add([12,5],[13,22]))#merging
c,d=map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34)#it returns result along with none

'''
'''
name,age,salary="balu",21,222222
#usage of return

def details():
    return name,age,salary
print(details())

There are  5types of arguments:
-->postional arguments
-->Default arguments
-->keyword arguments
-->variable length arguments(*args)
-->keyword variable length arguments(**kwargs)
'''
#positional Arguments --> Number of arguments in function defn should match with function call(order has to be maintained)
#print(len(123,234)) this is as per built-in len(obj) will accept one argument
'''
def details(name,place):
    """To store the details"""
    #name="balu"
    #place="hyd"
    return name,place
print(details("Balu","Codegnan"))
print(details("sai","vizag"))

def grocery(item,price=35):
    """usage of default arguments"""
    print(f'The item is{item} and the price is {price}')

grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread")#by default we have given price as 35
groceary()#as both item and price as default arguments
'''
#keyword arguments -->Whenever we want to specify the name of argument
def employee(name,salary,role):
    """KeyWord arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary}')
employee("sai",20000,"Admin")
employee("Akash",250000,"IT","Cognizant")
