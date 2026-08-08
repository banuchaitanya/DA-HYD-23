'''
secret_code = "1234"
while True:
    for i in range(1):
        code = input("Enter the secret code: ")
        if code == secret_code:
            print("Correct guess")
            break
        else:
            print("Wrong guess! Try again.")
    if code == secret_code:
        break
'''
#otp verification
'''
correct_otp = "1234"
for attempt in range(1, 8):
    otp = input("Enter OTP: ")
    if otp == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        print("Wrong OTP.")

        if attempt < 7:
            print("Try again.")
        else:
            print("You have used all 7 attempts. Verification failed.")
'''
#food order
'''
food=input()
count=0
while food!="exit":
    count+=1
    food=input()
print("total nuber of items ordered",count)
'''
