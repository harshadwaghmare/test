#!/usr/bin/python3

def wordspacesp(sentstr, dict):
    returnstr = ''
    for i in dict:
        if i in sentstr:
            returnstr += i + ' '
    print (returnstr)

def wordspacegn(sentstr, dict):
    returnstr = ''
    j = 0
    for i in range (len(sentstr) + 1):
        if sentstr[j:i] == ' ':
            i += 1
            j += 1
            continue
        if sentstr [j:i] in dict:
            returnstr += sentstr[j:i] + ' '
            j = i
    if not returnstr:
        return sentstr
    return returnstr

if __name__ == '__main__':
    dict = ['this', 'is', 'his', 'face']
    sentence = 'This is his face'
    print (wordspacegn (sentence, dict))