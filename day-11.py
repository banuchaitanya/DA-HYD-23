'''
Sequences--> Strings,Lists ,Tuples,Sets
Mapping--> Dictonary

#Lists--> Collection of heterogenous elements
#List-->Inexed,Ordered,Mutable
marks=[1,2,3,4]
print(marks)
print(len(marks))
print(type(marks))
'''
#operations :indexing,slicing,striding,Membership,merging,Repetition

#nested lists-->A list inside another list
names=['codegnan',25,4.6,[45,35,35,56],'Da23',33]
print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4])
print(names[0][4:])

'''
Sequences -->String,Lists,Tuples,Sets
Mapping -->Dictionary


#Lists --> Collection of heterogenous elements(item)
#List -->Indexed,Ordered,Mutable,Heterogenous,We use [] to score the data

marks = [35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#Operations : Indexing,Slicing,Strding,Merging,Repetition
'''

#Nested Lists --> A lists inside another list
'''
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(names)
print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4]) #it returns Code
print(names[0][4:])

#get the output as Cdga
print(names[0][0::2])
names[0] = names[0][::-1]
print(names)'''
'''
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing,Slicing -->Mutable
names[2] = 'python'
print(names)
#By indexing if we change tghe elements,length ofcollection will remain same
names[4] = ['Codegnan','PFS','DA','DS']
print(names)
print(len(names))
print(names[4][1:3])
print(names[4][0][4:])
''''''
names[2:4] = 'Abhiram','Sai''Hari','Ganesh'
print(names)
#In Slicing whatever elements u pass as per the logic length keeps on increase

#o/p as follows :
#['Codegnan',25,"Abhiram','Python','Hari','Java',,'DA23',.34}
names = ['codegnan','saketh']
#append() -->inserts single element to the end of the list
names.append(['analysis','agents'])
print(names)
#append() will always increment the length of list by 1
names(names[3])
names[3].append('chatgpt')
print(names)
'''
#extend()--> inserts mmultiple elements to the end of the list
names.extend('analysis')
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,34])
print(names)

