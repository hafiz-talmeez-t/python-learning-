students = [
    ("Ali", 78),
    ("Ahmed", 45),
    ("Usman", 92),
    ("Bilal", 55),
    ("Hamza", 38),
    ("Talmeez", 85)
]
pass_students=[]
highest_score=0
highest_scorer=''
failed_students=[]
for i in students:
    if i[1]>=50:
        pass_students.append(i[0])
    else:
        failed_students.append(i[0])
    if i[1]>highest_score:
        highest_score=i[1]
        highest_scorer=i[0]
print('the students who passed the paper are: ',pass_students)
print('the students who should try with more effort for next time are: ',failed_students)
print(f'the highest scorer is {highest_scorer} and he scored {highest_score}')
