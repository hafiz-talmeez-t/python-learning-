students = [
    ["Ali", 78, 85, 92],
    ["Ahmed", 65, 72, 68],
    ["Usman", 90, 88, 95],
    ["Bilal", 55, 60, 58]
    
]
highest_average=0
highest_student=0
average_70=0
for i in range(len(students)):
    total=0
    for j in range (1,len(students)):
        total+=students[i][j]
    average=total/(len(students[i])-1)
    print(f'{students[i][0]} have average {average} ')
    if average>highest_average:
        highest_average=average
        highest_student=students[i][0]
    if average>=70:
        average_70+=1
print('the student who has highest average is ',highest_student)
print(average_70,' students have average 70 or more')
