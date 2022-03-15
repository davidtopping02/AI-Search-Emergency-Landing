from apiInterfaces import *
from search import *

# creating new aircraft with flight number
flight_number = '3V812'
testAircraft = Aircraft(flight_number)

# creating new flight api interface
flight_api_interface = FlightApi(testAircraft)

# calling function to get required flight data from the api
testAircraft = flight_api_interface.get_data_from_api()

# printing the flight data to console
testAircraft.print_aircraft()
