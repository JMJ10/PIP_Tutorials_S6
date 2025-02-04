#Third largest number in the list
limit=int(input("Enter the number of list elements: "))
list1=[]
while limit>0:
    ele=int(input("Enter the element: "))
    list1.append(ele)
    limit-=1
print("List : ",list1)
list1.remove(max(list1))
list1.remove(max(list1))
print("3rd Largest Number in List : ",max(list1))