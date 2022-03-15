# This class gives the structure and suitable function for an aircraft object
class Aircraft:
    def __init__(self, flight_num=None,  direction=None, direction_compass=None, arrival_airport=None,  depart_airport=None, longitude=None, latitude=None, altitude=None, current_speed=None):
        self.flight_number = flight_num
        self.dir = direction
        self.dir_compass = direction_compass
        self.departure_airport = depart_airport
        self.arrival_airport = arrival_airport
        self.altitude = altitude
        self.longitude = longitude
        self.latitude = latitude
        self.current_speed = current_speed

    # Helper function to print out all fields of an aircraft object
    def print_aircraft(self):

        if self.departure_airport is not None:
            print("Flight number: " + self.flight_number)
            print("Departure airport:" + self.departure_airport)
            print("Arrival airport: "+ self.arrival_airport)
            print("Altitude: " + str(self.altitude))
            print("Longitude: " + str(self.longitude))
            print("Latitude: " + str(self.latitude))
            print("Current Speed: " + str(self.current_speed))
            print("Direction (degrees): " + str(self.dir))
            print("Direction (compass): " + str(self.dir_compass))
        else:
            return

    # calculates the compass direction of the aircraft based on the degrees
    def calc_direction(self):

        if self.dir == 360 or 0 <= self.dir < 45:
            str_dir = 'N'
        if 45 <= self.dir < 90:
            str_dir = 'NE'
        if 90 <= self.dir < 135:
            str_dir = 'E'
        if 135 <= self.dir < 180:
            str_dir = 'SE'
        if 180 <= self.dir < 225:
            str_dir = 'S'
        if 225 <= self.dir < 270:
            str_dir = 'SW'
        if 270 <= self.dir < 315:
            str_dir = 'W'
        if 315 <= self.dir < 360:
            str_dir = 'NW'

        self.dir_compass = str_dir

# class Airport:
