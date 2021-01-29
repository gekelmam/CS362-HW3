year = int(input("Enter the year:"))
if(year % 4== 0):
    if ((year % 100) == 0):
        if ((year % 400) == 0):
            print (str(year) + " Is a leap year.")
        else:
            print ("Not a leap year.")
    else:
        print (str(year) + " Is a leap year.")
else:
    print ("Not a leap year.")