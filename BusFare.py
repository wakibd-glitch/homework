class Vehicle:
    def __init__(self, seatCap, rate):
        self.seatCap = seatCap
        self.rate = rate

    def fare(self):
        return self.seatCap * self.rate


class Bus(Vehicle):
    def __init__(self, seatCap, repair, rate):
        super().__init__(seatCap, rate)
        self.repair = repair

    def totalFareWithRepair(self):
        base_fare = self.fare()   
        repair_cost = base_fare * (self.repair / 100)
        final_amount = base_fare + repair_cost
        return final_amount


busfare = Bus(20, 10, 100) #(seat capacity, repair percentage, rate(eg:seating * rate or seating * 100))
print(busfare.totalFareWithRepair())