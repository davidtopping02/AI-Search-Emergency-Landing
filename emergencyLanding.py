from apiInterfaces import *
from aviationDataStructures import *
from searchDataStructures import *


def problem_search(flight_number=None):
    data_retrieval = EmergencyProblem()
    data_retrieval.run_problem(flight_number)

    if len(data_retrieval.airports) == 0:
        print("\nYOU ARE GOING TO DIE GG")
        quit()
    else:
        the_problem = Problem([data_retrieval.aircraft.latitude, data_retrieval.aircraft.longitude],
                              data_retrieval.airports)
        Node = breadth_first_tree_search(the_problem)
        # Node = depth_first_tree_search(the_problem)
        # Node = breadth_first_graph_search(the_problem)
        coords = [the_problem.initial, Node.state]
        print("\nCoordinates of closest airport: " + str(Node.state))
        print("stop")

        return coords


class EmergencyProblem:

    def __init__(self, aircraft=None, airports=None):
        self.aircraft = aircraft
        self.airports = airports

    def run_problem(self, flight_number=None):
        self.get_aircraft_data(flight_number)
        self.get_airports()
        self.print_aircraft_airport()

    # gets all the info on an aircraft from its flight number
    def get_aircraft_data(self, flight_number):

        # creating temp aircraft
        temp_aircraft = Aircraft(flight_number)

        # Api call for aircraft data
        flight_api_interface = FlightApi(temp_aircraft)
        temp_aircraft = flight_api_interface.get_data_from_api()

        if temp_aircraft is None:
            print('error retrieving aircraft data')
            return None
        else:
            # setting the object's field
            self.aircraft = temp_aircraft
        # return the found aircraft
        return self.aircraft

    # gets up to the 10 closest airports to the aircraft
    def get_airports(self):

        # gets list of airports from api
        if self.aircraft is not None:
            airport_api_interface = AirportApi()
            airports = airport_api_interface.get_data_from_api(self.aircraft.latitude, self.aircraft.longitude)

            # setting the object's field
            self.airports = airports
        else:
            quit()

    def print_aircraft_airport(self):
        self.aircraft.print_aircraft()

        for x in range(len(self.airports)):
            self.airports[x].print_airport()
