class Staff:
    def __init__(self, name, idd, department):
        self.__name = name
        self.__id = idd
        self.__department = department
        
    def display(self):
        print(f"{self.__name} | {self.__id} | {self.__department}", end=" ")
    pass
        

class Teacher(Staff):
    def __init__(self, name, idd, department, course, salary):
        super().__init__(name, idd, department)
        self.__course = course
        self.__salary = salary
    
    def display(self):
        super().display()
        print(f"| {self.__course} | {self.__salary}")
    pass
        

class AdminStaff(Staff):
    def __init__(self, name, idd, department, role, working_hours):
        super().__init__(name, idd, department)
        self.__role = role
        self.__working_hours = working_hours

    def display(self):
        super().display()
        print(f"| {self.__role} | {self.__working_hours}")
    pass    
        

class ResearchAssistant(Staff):
    def __init__(self, name, idd, department, research_topic, stipend):
        super().__init__(name, idd, department)
        self.__research_topic = research_topic
        self.__stipend = stipend

    def display(self):
        super().display()
        print(f"| {self.__research_topic} | {self.__stipend}")
    pass


t = Teacher("Abdullah", "T1", "CS", "AI", 5000)
a = AdminStaff("Sara", "A1", "Admin", "Manager", "9-5")
r = ResearchAssistant("Ahmed", "R1", "Physics", "AI Research", 40000)

t.display()
a.display()
r.display()
