class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

class Manager(Employee):
    def __init__(self, name, salary, access):
        super().__init__(name, salary)
        self._access = access
    
    def displaydetails(self):
        print(f"{self._name} | {self._salary} | {self._access}")
        
Akbar = Manager("Akbar", 880, True)
Akbar.displaydetails()

Wasay = Manager("Wasay", 70, False)
Wasay.displaydetails()

Watermelon = Manager("Abdullah", 615, True)
Watermelon.displaydetails()

Omer = Manager("Omer", 625, True)
Omer.displaydetails()

Saud = Manager("Saud", 675, False)
Saud.displaydetails()

strawberry = Manager("Raseefa", 615, True)
strawberry.displaydetails()

Ani = Manager("Anahita", 650, False)
Ani.displaydetails()

Jarar = Manager("Jarar", 850, False)
Jarar.displaydetails()

Seniya = Manager("Seniya", 900, False)
Seniya.displaydetails()

Amrood = Manager("Amrood", 650, False)
Amrood.displaydetails()
