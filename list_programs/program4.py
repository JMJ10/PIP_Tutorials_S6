'''
program to take a list of integers. Create another list to store all the even
numbers from the master list and print the new list contents in ascending order
'''
limit=int(input("Enter the number of list elements: "))
list1=[]
while limit>0:
    ele=int(input("Enter the element: "))
    list1.append(ele)
    limit-=1
print("List : ",list1)
new_list=[]
for no in list1:
    if no%2==0:
        new_list.append(no)
new_list.sort()
print("New List : ",new_list)