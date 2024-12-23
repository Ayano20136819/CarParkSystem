import unittest
from car_park import CarPark
from pathlib import Path

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(capacity=100, location="123 Example Street")


    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.avaiable_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.avaiable_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.avaiable_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.avaiable_bays, 0)
        # Overfilling the car park should not change the number of available bays
        self.car_park.add_car("FAKE-100")
        self.assertEqual(self.car_park.avaiable_bays, 0)
        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.avaiable_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_log_file_created(self):
        new_car_park = CarPark(capacity=100, location="123 Example Street", log_file="new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    def tearDown(self):
        Path("new_log.txt").unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        new_car_park = CarPark("123 Example Street", 100, log_file="new_log.txt")
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as log_file:
            last_line = log_file.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("entered", last_line)
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        new_car_park = CarPark("123 Example Street", 100,
                              log_file="new_log.txt")
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as log_file:
             last_line= log_file.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_park_initialized_with_config_file(self):
        # Create a mock config file path
        config_file = Path("config.txt")

        # Initialize CarPark with the config_file parameter
        car_park = CarPark("123 Example Street", 100, config_file=config_file)

        # Check if the config_file attribute is correctly set
        self.assertEqual(car_park.config_file, config_file)

        # Optionally, check if the file exists (this assumes you want the file to exist for this test)
        # If you want to test with a real config file, make sure to create it or mock it
        self.assertTrue(config_file.exists())  # This will check if the file exists


if __name__ == "__main__":
   unittest.main()
