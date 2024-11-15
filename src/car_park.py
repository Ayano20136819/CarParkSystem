from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
class CarPark:
    def __init__(self, location, capacity,  plates=None, sensors=None,
                 displays=None,log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

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

        with open(self.log_file, 'a') as log_file:
            log_file.write(f"{plate} entered\n")

        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)

        with open(self.log_file, 'a') as log_file:
            log_file.write(f"{plate} exited\n")

        self.update_displays()

    def update_displays(self):
        for display in self.displays:
            display.update()

    @property
    def avaiable_bays(self):
        if len(self.plates) > self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)




if __name__ == '__main__':
    car_park = CarPark(capacity="Unknown", location="Unknown" )


