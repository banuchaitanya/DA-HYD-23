'''
usage of else with for --> the else keyword will only be executed when the loop is completely


'''
'''
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
        print(longest_streak)       
    else:
        current_streak =0
else:
    print(f'longest streak is {longest_streak}')
  '''
#for-else with notifications scenario
'''
notifications =[0,1,0,1]
for notification in notifications:
    if notification ==1:
        print('Unread notification')
        break
else:
    print('all caught up')
'''
#while--> it relies on condition ,it will be completely executed until the condition is satisfied...
'''
syntax while:
    statement(s)...
    ....
  '''
'''
while(True):
    print("Yes")
'''
'''
#it runs an infitnite loop we need to press ctrl+c (keyboard interupt)
i=10#initilised statement
while  i>=1:
        print(i)
        i=i-1#counter
'''
'''
#banking scenario -->PIN authentication if more than 3 attempts
#account locked
pin="2612"
max_attempts=3
current_attempt=0
while current_attempt< max_attempts:
        entered_pin= input("Enter the PIN:")
        if entered_pin == pin:
                print("login successful")
                break
        else:print("try again")
        current_attempt+=1
else:
        print("Account locked") 

'''
sum=0
for i in range(1,6):
        sum=sum+i
print(sum)
