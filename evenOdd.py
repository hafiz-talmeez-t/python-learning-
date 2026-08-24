numbers=[10,15,20,25,30,35,40,45]
new_list=[]
for i in numbers:
    if i%2==0:
        new_list.append(i**2)
    else:
        new_list.append(i**3)
print('the modified list is: ',new_list)
