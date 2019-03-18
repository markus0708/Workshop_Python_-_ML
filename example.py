
import numpy as np



class Student(object):
    schoolName = "deBritto"

    def __init__(self, name : str, nis : int):
        self.name = name
        self.nis = name

    def getEmail(self):
        return self.name + "@" + self.__class__.schoolName + ".com"


thomas = Student('thomas', 8976)
email = thomas.getEmail()

print ("Email name : ", email)
