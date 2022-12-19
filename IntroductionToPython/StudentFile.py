class Student():
    items =[]
    count =0
    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress
        Student.items.append(self)
        Student.count+=1


    def __str__(self):
        return f"Name:{self.name} - Group:{self.group} -Progress:{self.progress}"






