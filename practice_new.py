'''
def calculate_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "Fail"


for i in range(3):
    mark = int(input("Enter mark: "))
    grade = calculate_grade(mark)
    print("Mark:", mark, "Grade:", grade)

def calculate_bill(price, quantity=1, discount=0):
    total = price * quantity
    discount_amount = total * discount / 100
    final_bill = total - discount_amount
    return final_bill


print("Bill 1:", calculate_bill(100))

print("Bill 2:", calculate_bill(100, 3))

print("Bill 3:", calculate_bill(price=500, quantity=2, discount=10))

def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


for i in range(3):
    name = input("Enter name: ")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in metres: "))

    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)

    print("Name:", name)
    print("BMI:", round(bmi, 2))
    print("Category:", status)
    
def mark_summary(*args):
    total = 0

    if len(args) == 0:
        return 0, 0

    for mark in args:
        total = total + mark

    average = total / len(args)

    return total, average


total, average = mark_summary(80)
print("Total:", total)
print("Average:", average)

total, average = mark_summary(70, 80, 90)
print("Total:", total)
print("Average:", average)

total, average = mark_summary()
print("Total:", total)
print("Average:", average)
'''
def display_employee(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

    if "salary" in kwargs:
        print("Salary information is available")
    else:
        print("Salary information is missing")

    if "department" in kwargs:
        print("Department information is available")
    else:
        print("Department information is missing")


display_employee(name="Ramesh", age=24, salary=30000, department="IT")

print()

display_employee(name="Suresh", age=25, department="HR")

print()

display_employee(name="Anil", age=26, salary=35000)
