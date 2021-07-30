
with open ("t.txt") as fileobject:
    print (fileobject)
    for li in fileobject:
        print (li, end="")