n=float(input("Enter the number : "))
x=n/2
while True:
    f=(x+n/x)/2
    if abs(x-f)<1e-15:
        break
    x=f
print("Square root :",x)