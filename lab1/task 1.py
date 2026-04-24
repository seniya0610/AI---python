class Student:
    def __init__(self, roll, name, program):
        self._roll = roll
        self._name = name
        self._program = program

    def showdetails(self):
        print(f"{self._name} : {self._name} -> {self._program}")

s1 = Student("24K-0608", "Seniya", "Computer Science")
s2 = Student("24K-0770", "Khadija", "Computer Science")
s1.showdetails()
s2.showdetails()
