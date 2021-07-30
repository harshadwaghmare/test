#!/usr/bin/python3
from reversenum import reversenum

def ispalindrome (num):
    return num == reversenum (num)

def isstrpalindrome (str1):
    return str1 == str1[::-1]

if __name__ == '__main__':
        print (ispalindrome(12321))
        print (isstrpalindrome('12321'))