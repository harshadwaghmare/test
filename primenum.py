#!usr/bin/python3
import math
def primenum (num):
    for i in range (2, round(math.sqrt(num)) + 1):
        if not (num % i):
            return False
    return True
if __name__ == '__main__':
    num = int(input('Enter number : '))
    for i in range (1, num + 1):
        if primenum(i):
            print (i, end=' ')

    print ('')