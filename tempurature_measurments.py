days=['day1','day2','day3','day4','day5','day6','day7']
tempuratures={}
for i in days:
    tempurature=int(input(f'enter the temperature of {i}'))
    tempuratures[i]=tempurature
print('full temperature list: ',tempuratures)
highest_tempurature=max(tempuratures,key=tempuratures.get)
print('highest temperature : ',tempuratures[highest_tempurature])
minimum_tempurature=min(tempuratures,key=tempuratures.get)
print('lowest temperature: ',tempuratures[minimum_tempurature])
total_tempurature=0
hot_days=0
cold_days=0
for day,number in tempuratures.items():
    total_tempurature+=number
    if number>35:
        hot_days+=1
    if number<20:
        cold_days+=1
average_tempurature=total_tempurature/len(tempuratures)
print('average temperature: ',average_tempurature)
print('hot days: ',hot_days)
print('cold days: ',cold_days)

    
    
