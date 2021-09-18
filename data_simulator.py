from _global_imports import *
from _constants import *

fake = Faker()

def get_all_consumers():
    consumers_arr = []

    for _ in range(100):
        consumer = {}

        Vehicle = {}
        Vehicle["Registration_Number"] = str(fake.license_plate())
        Vehicle["Engine_Capicity"] = str(random.randrange(800, 3200, 400)) + "cc"
        Vehicle["Fuel_Type"] = ['Diesel', 'Petrol', 'Gas'][random.randrange(0,3)]
        Vehicle["Passenger_Limit"] = random.randrange(2,11)
        Vehicle["Vehicle_Color"] = fake.color_name()
        Vehicle["Heavy_Vehicle"] = [False, True][random.randrange(0,2)]
        Vehicle["Is_Commercial"] = [False, True][random.randrange(0,2)]

        Driver = {}
        Driver["Name"] = fake.name()
        Driver["License_Number"] = str(random.randrange(1554864658, 8515486644, 400))
        Driver["Occupation"] = str(fake.job())
        Driver["Country"]  = fake.city()

        #geolocator = Nominatim(user_agent="Your_Name")
        #location = geolocator.geocode(Driver["Country"])

        Sensor_Data = {}
        Sensor_Data["Timestamp"] = str(fake.iso8601()),
        Sensor_Data["Speed"] = str(random.randrange(60,150)) + "mph"
        #Sensor_Data["Latitude"] = str(location.latitude)
        #Sensor_Data["Longitude"] = str(location.longitude)
        Sensor_Data["Engine_Temperature"] = str(random.randrange(80, 160)) + "°C"
        Sensor_Data["Humidity"] = str(random.randrange(30, 95)) + "%"

        consumer["Vehicle"] = Vehicle
        consumer["Driver"] = Driver
        consumer["Sensor_Data"] = Sensor_Data

        consumers_arr.append(consumer)
    return consumers_arr

def get_next_data(consumers_arr):
    consumer_iteration_arr = []
    for consumer in consumers_arr:
        Sensor_Data = consumer["Sensor_Data"]
        Sensor_Data["Timestamp"] = str(datetime.now().time())
        Sensor_Data["Speed"] = str(random.randrange(60,150)) + "mph"
        Sensor_Data["Engine_Temperature"] = str(random.randrange(80, 160)) + "°C"
        consumer["Sensor_Data"] = Sensor_Data
        consumer_iteration_arr.append(consumer)
    return consumer_iteration_arr
