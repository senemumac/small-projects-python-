import time

year = int(input("Enter The Year: "))

def timer():
    epoch = time.gmtime()
    x = epoch.tm_year
    print("we are at ", format(x))
    leap(x)

def leap(year):
    if year %4 == 0 and year % 100 !=0:
        print("Leap year")
    elif year % 400 ==0:
        print("Leap Year")
    else:
        print("Not Leap Year") 
        # if year %100 == 0:   is also print("Not Leap Year")...
        
leap(year)
timer()
