from apiInterfaces import *
from aviationDataStructures import *
from searchDataStructures import *

the_aircraft = Aircraft('DP6531')
flight_api_interface = FlightApi(the_aircraft)
the_aircraft = flight_api_interface.get_data_from_api()

if the_aircraft is not None:
    emergency_landing = EmergencyLandingProblem(the_aircraft)
else:
    print("error retrieving aircraft data")
