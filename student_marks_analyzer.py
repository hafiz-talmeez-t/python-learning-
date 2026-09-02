name=input("enter student's name: ")
subjects=["maths","computer","bio","english","islamyat"]
marks=[]
total_marks=0
for i in range(5):
    m=int(input(f"enter the marks of {subjects[i]}"))   
    total_marks+=m
    marks.append(m)
average_marks=total_marks/len(subjects)
if average_marks>=40:
    print(f"many many congratulation {name} you are pass")
else:
    print(f"{name} try hard for the next time (fail)")
result={}
failed_subjects={}
fail_count=0
for subject,numbers in zip(subjects,marks):
    result[subject]=numbers
    if numbers<40:
        fail_count+=1
        failed_subjects[subject]=numbers
if fail_count>0:
    print("Subjects with marks below 40:", failed_subjects)
highest_marks=max(result,key=result.get)
print(f"total marks of {name} are {total_marks} with the  average of {average_marks}")
print(f"the highest subject marks of {name} are {result[highest_marks]} in subject {highest_marks}")


    
    
