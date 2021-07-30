#!usr/bin/python3

a = [2, 3, 4, 5, 6]

b = []
target = 7
ii, jj = 0, 0
flag = False
for i in a:
    jj = 0
    for j in a:
        if (ii < jj) and (i + j == target):
            print (ii, jj)
            flag = True
        jj += 1
    ii += 1

if not flag:
    print ("-1")

print ('End first')
flag = False
for i, val1 in enumerate(a):
    for j, val2 in enumerate(a):
        if (i < j) and (val1 + val2 == target):
            print (i, j)
            flag = True
        
if not flag:
    print ("-1")

