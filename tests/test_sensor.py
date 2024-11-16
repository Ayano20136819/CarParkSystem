import unittest
import random
import sensor
from car_park import CarPark
from sensor import Sensor
class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(location="TestLocation", capacity=100)
        self.sensor = sensor.EntrySensor(1, True, car_park=self.car_park)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, sensor.EntrySensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertIsInstance(self.sensor.car_park, CarPark)

    def test_detect_vehicle(self):
        car_park = CarPark(location="Perth", capacity=100)
        self.sensor = sensor.EntrySensor(id=1,is_active=True, car_park=car_park)
        self.sensor._scan_plate = lambda: 'FAKE-123'
        self.sensor.detect_vehicle()
        self.assertEqual('FAKE-123', self.sensor.detect_vehicle())


if __name__ == '__main__':
    unittest.main()