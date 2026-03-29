class Student:
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count+=1
    def show(self):
        print(self.name)
print("Total instance:", Student.count)
