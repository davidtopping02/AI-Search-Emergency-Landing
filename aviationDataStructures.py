# This class gives the structure and suitable function for an aircraft object
import math


class Aircraft:
    def __init__(self, flight_num=None, direction=None, direction_compass=None, arrival_airport=None,
                 depart_airport=None, longitude=None, latitude=None, altitude=None, current_speed=None):
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
            print("Arrival airport: " + self.arrival_airport)
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


class Airport:

    def __init__(self, airport_name=None, airport_city=None, latitude=None, longitude=None):
        self.airport_name = airport_name
        self.airport_city = airport_city
        self.airport_lat = latitude
        self.airport_long = longitude


    def print_airport(self):
        print(self.airport_name)
        print(self.airport_city)
        print(str(self.airport_lat))
        print(str(self.airport_long))
        print("\n")


def distance_between_coordinates(startPoint, endPoint):

    R = 6371.0  # radius of the earth

    # get lat and long from coordinate tuple
    lat1 = math.radians(startPoint[0])
    lon1 = math.radians(startPoint[1])
    lat2 = math.radians(endPoint[0])
    lon2 = math.radians(endPoint[1])

    # difference in lat and long
    dlat = lat1 - lat2
    dlon = lon1 - lon2

    # plug values into haversine equation
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance


def bearing_between_two_points(startPoint, endPoint):

    lat1 = math.radians(startPoint[0])
    lat2 = math.radians(endPoint[0])

    # snippet of code from https://gist.github.com/jeromer/2005586
    diffLong = math.radians(endPoint[1] - startPoint[1])
    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                                           * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    # print(compass_bearing, "degrees")

    return compass_bearing