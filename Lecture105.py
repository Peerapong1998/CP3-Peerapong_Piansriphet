
class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    name = ""
    def turnOnAirConditioner(self):
        print(self.name,": Turn On : Air")

class Car(Vehicle):
    pass

class Pickup(Vehicle):
     pass

class Van(Vehicle):
     pass

class Estatecar(Vehicle):
     pass

Car1 = Car()
Car1.name = "Car 4 seat"
Car1.turnOnAirConditioner()

Car2 = Pickup()
Car2.name= "Car Pickup"
Car2.turnOnAirConditioner()

Car3 = Van()
Car3.name = "Car Van"
Car3.turnOnAirConditioner()

Car4 = Estatecar()
Car4.name = "Estatecar"
Car4.turnOnAirConditioner()
