from car_park import CarPark
from sensor import EntrySensor, ExistSensor
from display import Display


#car01 = CarPark("123 Example Street",100)
#print(car01)

#create a car park object with the location moondalup, capacity 100, and log_file
# "moondalup.txt"
car_park = CarPark(location="moondalup", capacity=100, log_file="moondalup.txt")

# create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)

#  create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExistSensor(id=2, is_active=True, car_park=car_park)

car_park.register(entry_sensor)
car_park.register(exit_sensor)

#create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(1, message="Welcome to Moondalup", is_on=True, car_park=car_park)


# drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for car in range(10):
    entry_sensor.detect_vehicle()
print(f"Total cars in the car park: {len(car_park.plates)}")
print(f"Available bays: {car_park.avaiable_bays}")

# drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for car in range(2):
    exit_sensor.detect_vehicle()
print(f"Total cars in the car park after exit: {len(car_park.plates)}")
print(f"Available bays: {car_park.avaiable_bays}")

