class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.vid} - {self.model} ({self.year})"

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel, doors):
        super().__init__(vid, model, year)
        self.fuel = fuel
        self.doors = doors

    def __str__(self):
        return f"[Car] VID: {self.vid} | {self.model} ({self.year}) | Fuel: {self.fuel} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, load, axles):
        super().__init__(vid, model, year)
        self.load = load
        self.axles = axles

    def __str__(self):
        return f"[Truck] VID: {self.vid} | {self.model} ({self.year}) | Load: {self.load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, cc, mtype):
        super().__init__(vid, model, year)
        self.cc = cc
        self.mtype = mtype

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model} ({self.year}) | Eng: {self.cc}cc | Type: {self.mtype}"


def save_fleet_to_file(vlist, fname):
    f = open(fname, "w")
    for v in vlist:
        if isinstance(v, Car):
            line = f"Car,{v.vid},{v.model},{v.year},{v.fuel},{v.doors}\n"
        elif isinstance(v, Truck):
            line = f"Truck,{v.vid},{v.model},{v.year},{v.load},{v.axles}\n"
        elif isinstance(v, Motorcycle):
            line = f"Motorcycle,{v.vid},{v.model},{v.year},{v.cc},{v.mtype}\n"
        else:
            continue
        f.write(line)
    f.close()


def load_fleet_from_file(fname):
    arr = []
    f = open(fname, "r")
    for line in f:
        parts = line.strip().split(",")

        if parts[0] == "Car":
            obj = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
        elif parts[0] == "Truck":
            obj = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))
        elif parts[0] == "Motorcycle":
            obj = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])
        else:
            continue

        arr.append(obj)

    f.close()
    return arr


# test data
fleet = [
    Car("V001", "Car 1", 2024, "Electric", 4),
    Car("V002", "Car 2", 2015, "Petrol", 4),
    Truck("T101", "Truck 1", 2025, 25000, 6),
    Truck("T102", "Truck 2", 2010, 18000, 4),
    Motorcycle("M301", "Motor 1", 2023, 1000, "Sport"),
    Motorcycle("M302", "Motor 2", 2018, 250, "Cruiser")
]

save_fleet_to_file(fleet, "fleet.txt")

loaded = load_fleet_from_file("fleet.txt")

print("---All Vehicles---")
for v in loaded:
    print(v)

print("\n---Recent Vehicles (Last 4 Years)---")
for v in loaded:
    if v.is_new(4):
        print(v)

print("\n---Electric Cars Only---")
for v in loaded:
    if isinstance(v, Car) and v.fuel == "Electric":
        print(v)
