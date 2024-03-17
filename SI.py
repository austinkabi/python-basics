'''a program used to find simple interest'''
prin=int(input("enter principle"))
rate=int(input("enter  rate"))
time=int(input("enter time"))
SI=(prin*rate*time)/100
print(" {} multiplied by {} multiplied by {} divided by 100 to give SI {}".format(prin,rate,time,SI))