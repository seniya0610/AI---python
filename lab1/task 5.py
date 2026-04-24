class Light:
    def __init__(self, room_name):
        self._roomName = room_name
        self._status = "OFF"

    def turn_on(self):
        self._status = "ON"

    def turn_off(self):
        self._status = "OFF"

    def printstatus(self):
        print(self._status)
       
    def printname(self):
        print(self._roomName)

    def printdetails(self):
        print(f"{self._roomName} : {self._status}")


bedroom = Light("Bedroom")
washroom = Light("Washroom")
lounge = Light("Lounge")

bedroom.turn_on()
bedroom.turn_off()
washroom.turn_on()

washroom.printstatus()
bedroom.printdetails()
