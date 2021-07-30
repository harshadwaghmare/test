#!/usr/bin/python3
from factorialofnum import fact

def isstrongnum (num):
    digitfactsum = 0
    a = num
    while num > 0:
        digitfactsum += fact (num % 10)
        num = num // 10
    return digitfactsum == a

if __name__ == '__main__':
    for i in range (int (input("Enter limit : "))):
        if isstrongnum(i):
            print (i)