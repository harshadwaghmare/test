#!/usr/bin/python3
def reversenum (a):
    negative = False
    if a < 0:
        a = -1 * a
        negative = True
    newnum = 0
    while (a > 0):
        newnum = (newnum * 10) + (a % 10)
        a = a // 10

    if negative:
        newnum = -1 * newnum

    return newnum

if __name__ == '__main__':
    print (reversenum(1234))