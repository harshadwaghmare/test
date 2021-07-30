class hwparent:
    def __init__(self):
        print ("hello world.")

    def hwprint1(self):
        return 'hellow world'

class helloworld(hwparent):
    def __init__(self):
        super().__init__()
    def hwprint(self):
        return super().hwprint1()


hw = helloworld()
print (hw.hwprint())