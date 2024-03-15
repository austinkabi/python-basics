print("what is the answer of 5+5")
answer=int(input())
if answer==10:
    print("correct,5+5=10")
else:
    print("5+5 is not equal to{}".format(answer))
print("is someone eligible to vote")
age=int(input())
if age>=18:
    print("eligible to vote,>=18")
else:
    print("age not greater or equal to {} not eligible".format(age))
print("enter sales in ksh")
sales=int(input("enter sales"))
if sales >=50000:
    comm=2.5/100*sales
else:
    comm=0.5/100*sales
