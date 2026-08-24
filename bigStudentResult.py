students = [
    ("Ali", 72, 81, 69),
    ("Ahmed", 45, 52, 48),
    ("Usman", 91, 88, 95),
    ("Bilal", 63, 70, 58),
    ("Hamza", 38, 44, 41),
    ("Talmeez", 85, 79, 90)
]
perfect_student=''
highest_student_average=0
python_marks=0
math_marks=0
statistics_marks=0
for i in students:
    total=0
    for j in range (1,len(students[0])):
        total+=i[j]
        if j==1:
            python_marks+=i[j]
        elif j==2:
            math_marks+=i[j]
        else:
            statistics_marks+=i[j]
    average=total/(len(i)-1)
    if average>highest_student_average:
        perfect_student=i[0]
        highest_student_average=average
    if average>=80:
        performance="excellent"
    elif average>=60:
        performance='good'
    elif average>=50:
        performance='average'
    else:
        performance='poor'
    print(f'the average of {i[0]} is {average}and his performance is {performance}')
python_average=python_marks/len(students)
maths_average=math_marks/len(students)
statistics_average=statistics_marks/len(students)
if python_average>maths_average:
    if python_average>statistics_average:
        highest_average_s='python'
    else:
        highest_average_s='statistics'
elif maths_average>python_average:
    if maths_average>statistics_average:
        highest_average_s='maths'
    else:
        highest_average_s='statistics'
else:
    highest_average_s='statistics'
print(f'the student with average is {perfect_student} and his average is {highest_student_average}' )
print(f'{highest_average_s} has the highest average')
print()
print('extra information')
print('maths',maths_average)
print('statistics',statistics_average)
print('python',python_average)
