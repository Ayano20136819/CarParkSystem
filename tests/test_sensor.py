import unittest
import random
import sensor
from car_park import CarPark
from sensor import Sensor
class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = sensor.EntrySensor(1, True, CarPark)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, sensor.EntrySensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertIsInstance(self.sensor.car_park, CarPark)

    def test_detect_vehicle(self):
        car_park = CarPark(location="Perth", capacity=100)
        self.sensor = Sensor(car_park)
        sensor.plates = ['FAKE-123']
        self.sensor.detect_vehicle()
        self.assertEqual(self.sensor.detect_vehicle(),'FAKE-123')

