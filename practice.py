'''
products=list(map(int,input("Enter the prices:").split(',')))
total=0
for i in products:
    total=total+i
print("Total value is ",total)
'''
password=input("Enter the password:")
upper=0
lower=0
digit=0
special=0
for i in password:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    else:
        special+=1
print("Uppercase:",upper)
print("Lowercase:",lower)
print("Digits:",digit)
print("Special characters:",special)
