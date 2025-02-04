'''
program to take two list of integers and return a list containing the elements
that are common in both the list. Also print the contents of new list.
'''
limit1=int(input("Enter the number of list 1 elements: "))
list1=[]
while limit1>0:
    ele=int(input("Enter the element of list 1: "))
    list1.append(ele)
    limit1-=1
print("List 1: ",list1)
limit2=int(input("Enter the number of list 2 elements: "))
list2=[]
while limit2>0:
    ele=int(input("Enter the element of list 2: "))
    list2.append(ele)
    limit2-=1
print("List 2: ",list2)
new_list=[]
for no in list1:
    if no in list2:
        new_list.append(no)
print("New List : ",new_list)
