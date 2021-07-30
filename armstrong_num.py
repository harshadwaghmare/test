#!/usr/bin/python3

def isarmstrong(num):
    a = num
    cubesum = 0
    while a > 0:
        cubesum += ((a%10)**3)
        a = a // 10
    return cubesum == num
    
if __name__ == '__main__':
    for i in range (1000):
        if isarmstrong(i):
            print (i)