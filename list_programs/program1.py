#Largest and Smallest nos in a list
limit=int(input("Enter the number of list elements: "))
list1=[]
while limit>0:
    ele=int(input("Enter the element: "))
    list1.append(ele)
    limit-=1
print("List : ",list1)
print("Largest element : ",max(list1))
print("Smallest element : ",min(list1))