# This class gives the structure and suitable function for an aircraft object
class Aircraft:
    def __init__(self, flight_num=None,  arrival_airport=None,  depart_airport=None, longitude=None, latitude=None, altitude=None, current_speed=None):
        self.flight_number = flight_num
        self.departure_airport = depart_airport
        self.arrival_airport = arrival_airport
        self.altitude = altitude
        self.longitude = longitude
        self.latitude = latitude
        self.current_speed = current_speed

    # Helper function to print out all fields of an aircraft object
    def print_aircraft(self):
        print("Flight number: " + self.flight_number)
        print("Departure airport:" + self.departure_airport)
        print("Arrival airport: "+ self.arrival_airport)
        print("Altitude: " + str(self.altitude))
        print("Longitude: " + str(self.longitude))
        print("Latitude: " + str(self.latitude))
        print("Current Speed: " + str(self.current_speed))


