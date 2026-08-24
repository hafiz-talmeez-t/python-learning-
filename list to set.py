list1=[10,20,30,40,50,20,30]
list2=[30,40,50,60,70,40]
list1=set(list1)
list2=set(list2)
union=list1.union(list2)
common=list1.intersection(list2)
in_list1_only=list1.difference(list2)
in_list2_only=list2.difference(list1)
n=len(union)
print('all elements that appear in either list are: ',union)
print('the elements which are in common in both list are: ',common)
print('the elements which are only in list number 1 are: ',in_list1_only)
print('the elements which are only in list number 2 are: ',in_list2_only)
print(n,'are the different elements in either list')
