tot_income=float(input("Enter the total income : "))
n_dep=int(input("Enter the no. of dependents : "))
deducts=n_dep*30000.0
tax_income=tot_income-deducts
print("Taxable Income : ",tax_income)
tax_rate=0.0
if tax_income<250000:
    tax_rate=0
elif tax_income>=250000 and tax_income<500000:
    tax_rate=0.05
elif tax_income>=500000 and tax_income<750000:
    tax_rate=0.1
elif tax_income>=750000 and tax_income<1000000:
    tax_rate=0.15
elif tax_income>=1000000 and tax_income<1250000:
    tax_rate=0.2
elif tax_income>=1250000 and tax_income<1500000:
    tax_rate=0.25
else:
    tax_rate=0.3
tax_amount=tax_rate*tax_income
print("Tax to be paid :",tax_amount)