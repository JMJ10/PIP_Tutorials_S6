initial=int(input("Enter the initial investment amount: "))
interest=float(input("Enter the interest percentage: "))
years=int(input("Enter the number of years of investment: "))

int_rate=interest/100
inv_value=initial

print("-------Investment Report-------")
for y in range(years):
    inv_value+=inv_value*int_rate
    print("Year :",y+1,"-> Value : Rs",format(inv_value,".2f"))
growth=inv_value-initial

print("Final Amount : Rs",format(inv_value,".2f"))
print("Growth : Rs",format(growth,".2f"))

