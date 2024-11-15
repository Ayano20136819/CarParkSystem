from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    def __init__(self, location, capacity,  plates=None, sensors=None,
                 displays=None,log_file=Path("log.txt"), config_file=Path("config.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.config_file.touch(exist_ok=True)
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

        #with open(self.log_file, 'a') as log_file:
            #log_file.write(f"{plate} entered\n")

        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)

        #with open(self.log_file, 'a') as log_file:
            #log_file.write(f"{plate} exited\n")

        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        for display in self.displays:
            display.update()

    @property
    def avaiable_bays(self):
        if len(self.plates) > self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as log_file:
            log_file.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def write_config(self):
        with open("config.json",
                  "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

if __name__ == '__main__':
    car_park = CarPark(capacity="Unknown", location="Unknown" )


