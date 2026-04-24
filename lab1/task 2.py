class SmartFan:
    def __init__(self, roomName):
        self._speed = 0
        self._roomName = roomName
        self._status = "off"

    def turn_on(self):
        self._status = "on"

    def turn_off(self):
        self._status = "off"
   
    def increase_speed(self, increase):
        if self._status == "on":
            self._speed += increase
            if self._speed > 100:
                self._speed = 100
                print("Fan at max speed (100)")
        else:
            print("Fan is off. Please turn on fan")

    def decrease_speed(self, decrease):
        if decrease >= self._speed:
            self._speed = 0
            self._status = "off"
            print("Fan has been turned off")
        else:
            self._speed -= decrease

    def show_status(self):
        print(f"{self._roomName} | Status: {self._status} | Speed: {self._speed}")


fan1 = SmartFan("Living Room")
fan2 = SmartFan("Bedroom")
fan3 = SmartFan("Washroom")
fan4 = SmartFan("Hall")

fans = [fan1, fan2, fan3, fan4]

fan1.turn_on()
fan1.increase_speed(30)
fan1.increase_speed(90)

fan2.turn_on()
fan2.increase_speed(30)
fan2.decrease_speed(50)

fan3.turn_on()
fan3.increase_speed(80)
fan3.decrease_speed(20)

for fan in fans:
    fan.show_status()
