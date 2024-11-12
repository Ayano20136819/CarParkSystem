class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Car Park at {self.location}, with {self.capacity} bays"

if __name__ == '__main__':
    car_park = CarPark("Unknown","Unknown" )


