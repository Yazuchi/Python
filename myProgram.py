class Vehicle:
    pass

class Vehicle:
    engine_capacity = "1,6 Turbo"

class Vehicle:
    def __init__(self,number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        print("The vehicle is in driving mode now.")

vios = Vehicle ('4','petrol', 5,180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)

vios.drive()

class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)


blueSG = ElectricCar('4', 5, 150)
blueSG.drive()

class Computer:
    pass

class Computer:
    capability = "Dark Souls"

class Computer:
        def __init__(self, number_of_cores, type_of_ram, computer_type, maximum_storage):
            self.number_of_cores = number_of_cores
            self.type_of_ram = type_of_ram
            self.computer_type = computer_type
            self.maximum_storage = maximum_storage

        def playGame(self):
            print(" Dark Souls is being played.")

apple = Computer (4, '16GB', 'Desktop','1TB')
print(apple.number_of_cores)
print(apple.type_of_ram)
print(apple.computer_type)
print(apple.maximum_storage)

apple.playGame()


class laptop(Computer):
    def __init__(self, number_of_cores, type_of_ram, maximum_storage):
        Computer.__init__(self, number_of_cores, type_of_ram, 'laptop', maximum_storage)

lenovo = laptop(4,'16GB', '1TB')
lenovo.playGame()

class desktop(Computer):
    def __init__(self, number_of_cores, type_of_ram, maximum_storage):
        Computer.__init__(self, number_of_cores, type_of_ram, 'desktop', maximum_storage)

asus = desktop(4,'16GB', '1TB')
asus.playGame()