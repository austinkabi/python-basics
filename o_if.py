print("enter sales in ksh")
sales=int(input("enter sales"))
if sales >=50000:
    comm=2.5/100*sales
else:
    comm=0.5/100*sales
print("your sales is {} and your comm is {}".format(sales,comm))