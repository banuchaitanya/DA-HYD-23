'''
Control statements-->control of flow of execution of the program
--> conditional staments--> if,elif,else,..
-->Repetation statements (Loops) -->for while(for with else)
-->Jumping Statements -->break,continue,pass
'''
#Loops --> Loops are helpful for repetatio(automative tasks)
#for keyword will be helpful to iterativeover a sequence /range
#syntax for (for keyboard:
'''
for <temp_var> in sequence/range:
   statement(s)..,
   .....
'''
'''
#range (start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)'''
'''#In above case we got 10 iterations
for i in range(1,10):
    if i >5:
        print(f'value of is -->{i}')
'''        '''
for i in range(1,10):
    if i > 5 and i%2 == 0:
        print(f'Final value of i is -->{i}')
'''
'''
#range(Start,stop,step)--> here step-->interval..
for i in range(-10,-0,1):
    print(i)
'''
#[] --> we generally Lists
'''
names = ['Balu','ajay','kowshik']
print(len(names))#len obj -->returns the number of items in a container
for name in names:
    #print(name)
    #print(f'Student name is {name}')
    if name=="sai":
        print(f"student name is {name}")
'''
'''
result=0 #target variable
for i in range(21):
    if i%2==0:
        print (i)
        #print(f'result is {i+i}')
        result =result+i #result =+ i
        print(f'sum of 10 even numbers is  {result}')
'''
#Understand the loops usage with fitness streak example
#work_out -->1,work_out_missed -->0
work_log =[0,1,1,1,1,1,0,1,0]
#result variable--> longest_streak
longest_streak=0
current_streak=0
for day in work_log:
    if day ==1 :
        #print(day)
        current_streak = current_streak+1
    if current_streak > longest_streak:
        longest_streak = current_streak
        
    else:
        current_streak =0
print(longest_streak)    
