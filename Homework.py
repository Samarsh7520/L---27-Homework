class vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class bus(vehicle):
    def fare(self):
        amt = super().fare()
        amt = amt + amt * 0.2
        return amt


obj = bus("Volvo", 40)
print("Bus fare:", obj.fare())
