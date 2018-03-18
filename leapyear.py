year1 =int(input("Enter a year: "))
if (year1 % 4) == 0:
   if (year1 % 100) == 0:
       if (year1 % 400) == 0:
           print("{0} is a leap year1".format(year1))
       else:
           print("{0} is not a leap year1".format(year1))
   else:
       print("{0} is a leap year1".format(year1))
else:
   print("{0} is not a leap year1".format(year1))
