class Vehicle:
    def __init__(self, Name):
        self._Name = Name

    def start(self):
        print(f"Start Vehicle ({self.__Name})")
    
class Car(Vehicle):
    def __init__(self, Name):
        super().__init__(Name)
    
    def start(self):
        print(f"Start Car ({self._Name})")
    
class Bike(Vehicle):
    def __init__(self, Name):
        super().__init__(Name)
        
    def start(self):
        print(f"Start Bike ({self._Name})")
    
class Bus(Vehicle):
    def __init__(self, Name):
        super().__init__(Name)
        
    def start(self):
        print(f"Start Bike ({self._Name})")

vehicles = [Car("RollsRoyce"), Bike("Kawasaki"), Bus("School Bus")]

#for x in vehicles:
#    x.start()

for i in range(len(vehicles)):
    vehicles[i].start()
