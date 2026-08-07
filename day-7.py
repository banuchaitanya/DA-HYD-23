#calculate a batsman's innings
'''
total_score = 0
boundaries = 0
dot_balls = 0
balls = int(input("Enter the number of balls faced: "))
for i in range(1, balls + 1):
    runs = int(input(f"Enter runs scored on ball {i}: "))
    total_score += runs
    if runs == 0:
        dot_balls += 1
    if runs == 4 or runs == 6:
        boundaries += 1
print("\n----- Innings Summary -----")
print("Balls Faced :", balls)
print("Total Score :", total_score)
print("Boundaries  :", boundaries)
print("Dot Balls   :", dot_balls)
'''
#check PIN with 5 attempts
'''
correct_pin = "1234"
attempts = 5
while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Phone Unlocked")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Wrong PIN!")
            print("Attempts left:", attempts)
        else:
            print("Phone Locked")
'''
#
