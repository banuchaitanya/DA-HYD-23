'''
Lists,Tuples,.
'''
#Lists--> Mutable,Ordered,heterogenous

#index(),count(),copy(),sort(),reverse()
'''
details=['codegnan',7,2018,'hyd']
print(len(details))
print(details.index(7))
details.extend([7,21,45,21])
print(details.index(21))#it returns first occurance
print(details.index(21,6))
#print(details.index('python'))#valueerror

print(details.count(21))
print(details.count('python'))#it returns 0 as we dont have it


data=['cd','balu','python','java']
'''
#output should follows like this
'''
0:cd
1:balu
2:python
3:java

for obj in range(len(data)):
    print(obj,':',data[obj])
'''
#copy()--> shallow copy of the given collection
'''
new=data.copy()
print(new)
print(type(new))
print(len(data))

new[2]='Agentic AI'
print(new)
print(data)

data.append('balu')
print(data)
print(new)

new[3][2]='Agents'#whenever we make changes in nested ort=iginal lists will also effectd
print(new)
print(data)

new[1]='python'
print(new)
print(data)
'''
'''
marks=[14,22,44,33,-43]
print(marks)
#print.sort()#returns none
#print(marks)#returns in ascending order
#marks.sort(reverse=True)
#print(marks)
marks.reverse()
print(marks)
print(marks[::-1])
'''
#type(),len(),max(),min(),print()
'''
print(sorted('codegnan'))#returns list in ascending order
#print(sorted(['code',23,44]))#raises Error
'''
#Tuples-->Tuples are indexed,ordered,Heterogenous,Immutable,collection
#dimensions,coordinates,databases,records -- we perfer () for tuple notation
'''
a=()
print(type(a))
print(len(a))
'''
#opertions--> Indexng,slicing,striding,Membership,merging, repetation
'''
courses=('PFS','JFS',('DA','DS'),'Agnetic AI',[100,6,6])
print(courses)
print(len(courses))

print(courses[-2][-2:])
#courses[2]=23 tuples are immutable
courses[-1].append('codegnan')#we can make any modifications inside tuple
print(courses)

#create a Nested tuple as above and work on slicing,striding and list fuction
print('PFS'in courses)#membership
d=courses*2#repetation
print(d)
e= courses+(2,3,4,5)#merging
print(e)
'''
#Tuples Immutable--> count(),index()
'''
print(courses.index('Agentic AI'))#returns first occurance
print(courses.count('agents'))

#print(courses.sort())#attributeError -->sort() is in lists not in tuples
print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed type

#Typecasting
d=tuple(Sorted((23,12,3,4,5)))
print(d)
'''
a=eval(input("Enter a list:"))
print(a)
print(type(a))

#Task: Take a user input  as string,do this in two ways...
'''
1) Give the count of each repeating character\
test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is reapating 2 times

2.
r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is reapating 2 times
index=[6,7]
