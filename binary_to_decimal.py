bin_no=input("Enter the Binary No: ")
dec_no=0
bin_digit=0
power=len(bin_no)-1
for digit in bin_no:
    dec_digit=0
    bin_digit=int(digit)
    if bin_digit==1:
        dec_digit=2**power
    power-=1
    dec_no+=dec_digit
print("Decimal No:",dec_no)