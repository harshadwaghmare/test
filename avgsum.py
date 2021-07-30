#!/usr/bin/python3

def avgsum():
    n = input ()

    a = n.split(" ")
    sum_a = 0
    for i in a:
        try :
            temp_i = int (i)
        except ValueError:
            print ("Enter Valid Numbers")
            avgsum()
        sum_a += temp_i
    return sum_a/len(a)

def sumofdigit (num):
    sum_num = 0
    while (num > 0):
        sum_num += num % 10
        num = num // 10
    return sum_num

if __name__ =='__main__':
    #print (avgsum())
    while (True):
        try :
            inp_num = int (input("Enter Number : "))
            break
        except ValueError:
            print ("Enter Valid Number. Try Again!")
            continue
        except Exception:
            break
    print (sumofdigit(inp_num))
