
class Vehicle:
    color="white"
    def __init__(self,name,max_speed,mileage,capacity):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity


    def congrats(self):
      return f"Hello Nalenyi congratulations for buying a {self.color} {self.name} that goes by {self.max_speed} in {self.mileage}  "
    def name (self):
        return f"{self.name} carries{self.capacity} "
