# program to take a list of integers. Create another list with those numbers in the master list that are less than a number entered by the user. Print the new list contents.
limit=int(input("Enter the number of list elements: "))
list1=[]
while limit>0:
    ele=int(input("Enter the element: "))
    list1.append(ele)
    limit-=1
print("List : ",list1)
num=int(input("Enter a number : "))
new_list=[]
for no in list1:
    if no<num:
        new_list.append(no)
print("New List : ",new_list)