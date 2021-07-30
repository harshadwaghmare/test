#!/usr/bin/python3

def numofvowels(stra):
    counter = 0
    for i in stra:
        if i in 'aeiouAEIOU':
            counter += 1
    return counter

def commonletters (str1, str2):
    return list (set(str1)&set (str2))

if __name__ == '__main__':
    #print (numofvowels('tst'))
    for i in commonletters('abcd', 'cde'):
        print (i)