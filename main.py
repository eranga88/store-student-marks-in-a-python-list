student = []
results_list = []

while True:
    id = int(input("Student ID : "))

    id_existing = False

    for p in results_list:
        if id == p[0]:
            print("You have already entered student number : " + str(id) + ". Please enter new student number.")
            id_existing = True

    if id_existing:
        continue

    if id == 0:
        break
    elif id < 0:
        print("Please Enter valid Student number")
        continue


    student.append(id)

    input1 = 0

    while True:
        input1 = float(input("Enter Q1: "))
        if input1 < 0 or input1 > 20:
            print("Enter valid mark for Q1")
            continue
        else:
            break
    student.append(input1)

    input2 = 0

    while True:
        input2 = float(input("Enter Q2: "))
        if input2 < 0 or input2 > 30:
            print("Enter Valid mark for Q2")
            continue
        else:
            break
    student.append(input2)

    input3 = 0

    while True:
        input3 = float(input("Enter Final: "))
        if input3 < 0 or input3 > 50:
            print("Enter Valid Final Mark")
            continue
        else:
            break
    student.append(input3)

    total = input1 + input2 + input3

    student.append(total)

    grade = ""

    if 80 <= total <= 100:
        grade = "HD"
    elif 70 <= total < 80:
        grade = "D"
    elif 60 <= total < 70:
        grade = "C"
    elif 50 <= total < 60:
        grade = "P"
    elif total < 50:
        grade = "N"

    student.append(grade)

    results_list.append(student)

    student = []

print(results_list)

##############  Question 3   #############


tot_mark = 0.0
min = 0.0
max = 0.0
failed = 0
students_highest_marks = []
students_lowest_marks = []

min = results_list[0][4]
for st in results_list:
    tot_mark = tot_mark + st[4]

    if st[4] > max:
        max = st[4]

    if st[4] < min:
        min = st[4]

    if st[5] == 'N':
        failed = failed + 1


for x in results_list:
    if max == x[4]:
        students_highest_marks.append(x[0])
    if min == x[4]:
        students_lowest_marks.append(x[0])

number_of_students = len(results_list)

avg_mark = tot_mark/number_of_students

print("Average of the Unit : ",avg_mark)
print("Highest mark of the Unit : ",max)
print("Lowest mark of the Unit : ",min)
print("The ID of all the students who got the highest mark : ",students_highest_marks)
print("The ID of all the students who got the lowest mark : ",students_lowest_marks)
print("Total number of students failed in the unit : ",failed)
