raw_website_logs = [
    (501, 150.25, "Canada"),
    (502, 45.00, "USA"),
    (503, 1200.00, "UK"),
    (501, 150.25, "Canada"),       
    (504, 85.50, "Germany"),
    (505, 950.00, "USA"),
    (503, 1200.00, "UK"),         
    (506, 620.00, "Australia"),
    (507, 15.00, "Canada"),
    (502, 45.00, "USA")           
]
unique_countries=set()
clean={}
for i in raw_website_logs:
    unique_countries.add(i[2])
    if i[0] in clean:
        if i[1]>clean[i[0]]:
            clean[i[0]]=i[1]
    else:
        clean[i[0]]=i[1]

            
tier1=[]
tier2=[]
tier3=[]

for address,total in clean.items():
    if total>500:
        tier1.append(address)
    elif total>100:
        tier2.append(address)
    else:
        tier3.append(address)
print(f"Tier 1 costumers: {tier1}")
print(f"Tier 2 costumer: {tier2}")
print(f"Tier 3 costumer: {tier3}")
print(f"countries where we should show ads more: {list(unique_countries)}")

