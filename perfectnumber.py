#!/usr/bin/python3

def isperfectnum(num):
    sumofdivisors = 0
    for i in range(1, (num // 2) + 1):
        if not (num % i):
            sumofdivisors += i
    return sumofdivisors == num
if __name__ == '__main__':
    for i in range (1000):
        if isperfectnum(i):
            print (i)
