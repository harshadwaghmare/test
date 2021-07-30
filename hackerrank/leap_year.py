#!/usr/bin/python3

def is_leap (year):
    leap = False
    if not (year % 4):
        leap = True
        if not (year % 100) :
            if not (year % 400):
                leap = True
            else:
                leap = False
    return leap

#print (is_leap(int(input("Enter Year : "))))
i = 1850
while i < 2100:
    if is_leap(i):
        print ("( " + str(i) + " ) - leap year\n")
    else :
        print (i, end=" ")
    i += 1