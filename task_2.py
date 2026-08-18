'''
marks = []

for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("Original marks:", marks)

marks.insert(0, 90)

marks.extend([75, 85])

print("After adding 90, 75 and 85:", marks)

if 75 in marks:
    marks.remove(75)
    print("75 removed")

removed = marks.pop()
print("Removed final mark:", removed)

print("Final marks:", marks)
print("Number of marks:", len(marks))

numbers = [20, 10, 30, 20, 40, 20]

numbers.sort()
print("Ascending order:", numbers)

numbers.reverse()
print("Descending order:", numbers)

search = int(input("Enter a number to search: "))

if search in numbers:
    print("Number found")
    print("Count:", numbers.count(search))
    print("First index:", numbers.index(search))
else:
    print("Number not found")

print("Smallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total:", sum(numbers))

for number in numbers:
    print("Number:", number)

numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even numbers:", even)
print("Odd numbers:", odd)

print("First three values:", numbers[:3])
print("Last three values:", numbers[-3:])

backup = numbers.copy()

numbers.clear()

print("Original list after clear:", numbers)
print("Backup list:", backup)

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

unique_names = set(names)

unique_names.add("Meera")

unique_names.update(["Arun", "Priya"])

if "John" in unique_names:
    unique_names.remove("John")

unique_names.discard("David")

print("Unique names:")

for name in unique_names:
    print(name)
'''
python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

# Students from both courses
both_courses = python_students.union(da_students)

# Students learning both courses
common_students = python_students.intersection(da_students)

# Students only in Python
only_python = python_students.difference(da_students)

# Students learning only one course
only_one = python_students.symmetric_difference(da_students)

print("Students from both courses:", both_courses)
print("Students learning both courses:", common_students)
print("Students only in Python:", only_python)
print("Students learning only one course:", only_one)

# Relationship checks
print("DA is subset of Python:", da_students.issubset(python_students))
print("Python is superset of DA:", python_students.issuperset(da_students))
print("Courses are disjoint:", python_students.isdisjoint(da_students))

# Loop to display common students
print("\nCommon students:")
for student in common_students:
    print(student)

# Condition
if common_students:
    print("Rahul and Meera are learning both courses.")
else:
    print("No students are learning both courses.")
