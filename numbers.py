numbers=[12,5,8,12,20,5,7,30,12,9,8,5]
highest_occurance=0
number_most=0
single_time=[]
for i in numbers:
    if numbers.count(i)>highest_occurance:
        highest_occurance=numbers.count(i)
        number_most=i
    if numbers.count(i)==1:
        single_time.append(i)
print(f'the number which occured the most is {number_most} and it occured {highest_occurance} times')
print('these are the numbers which occured only one time are: ',single_time)
