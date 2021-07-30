#!/usr/bin/python3
def testfunc(arg1, arg2 = ''):
	if arg2:
		print (arg1 + ' if block ' + arg2 )
	else:
		print (arg1)

testfunc ('harshad', 'akot')
testfunc ('harshadaasdfsdf')


def fibo (a) :
	if a > 1:
		return a * fibo (a-1)
	else:
		return 1
 
a = fibo(int (input ('number : ')))
print (a)

class Test:
        def __init__(self, typ):
                self.typ = typ
        def ts(self, name):
                return name, self.typ

t = Test('new class')
print (t.ts("harshad:"))

