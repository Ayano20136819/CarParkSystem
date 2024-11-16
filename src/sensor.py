from abc import ABC, abstractmethod

import random

class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 9999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def __init__(self, id, is_active, car_park):
        super().__init__(id, is_active, car_park)

    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected. Plate: {plate}")

class ExistSensor(Sensor):

    def __init__(self, id, is_active, car_park):
        super().__init__(id, is_active, car_park)
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)

