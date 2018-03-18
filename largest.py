no1=int(input("enter a number"))
no2=int(input("enter a number"))
no3=int(input("enter a number"))
if (no1 >= no2) and (no1 >= no3):
   largest = no1
elif (no2 >= no1) and (no2 >= no3):
   largest = no2
else:
   largest = no3

print("The largest number between",no1,",",no2,"and",no3,"is",largest)
