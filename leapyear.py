year = 2016
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("2016 is a leap year")
       else:
           print("2016  is not a leap year")
   else:
       print("2016  is a leap year")
else:
   print("2016  is not a leap year")
