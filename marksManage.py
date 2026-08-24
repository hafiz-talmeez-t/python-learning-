marks=[72,45,89,63,91,38,76,55,84,67]
maximum=marks[1]
minimum=marks[1]
pass_count=0
fail_count=0
total_marks=0
for i in marks:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
    if i>=50:
        pass_count+=1
    if i<50:
        fail_count+=1
    total_marks+=i
average=total_marks/len(marks)
print('maximum marks are : ',maximum)
print('minimum marks are : ',minimum)
print(f'{pass_count} students passed the exam')
print(f'{fail_count} students failed ')
print('average marks of all students is: ',average)
