from sensor import Sensor
from display import Display
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

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)

        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_display()

    def update_displays(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")

    @property
    def avaiable_bays(self):
        if self.plates > self.capacity:
            return 0
        return self.capacity - len(self.plates)




if __name__ == '__main__':
    car_park = CarPark("Unknown","Unknown" )


