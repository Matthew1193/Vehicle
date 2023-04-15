class Vehicle:
    def __init__(self, brand = "", color = "", type = "", fuel = "", reg = "", year = 0, ID = 0):
        self.brand = brand
        self.color = color
        self.fuel = fuel
        self.type = type
        self.reg = reg
        self.year = year
        self.ID = ID

class Service:
    def __init__(self, hours = 0, prio = 1, cost = 0, ID = 0):
        self.hours = hours
        self.prio = prio
        self.cost = cost
        self.ID = ID

class CarSmart:
    my_list = []
    def read_vehicles(self, file_name):
        self.vehicles = []
        self.services = []

    def __repr__(self):
        return f"MyClass(i={self.vehicles}, j={self.services})"

    with open('vehicles.txt') as f:
        rows = [r.strip().split(',') for r in f.readlines()[:8]]
        my_list.append(Vehicle(*row) for row in rows)

    for obj in my_list:
        print(obj.brand, obj.color, obj.fuel, obj.type, obj.reg, obj.year, obj.ID)

    print(my_list)

#int(len(f.readlines()))
   