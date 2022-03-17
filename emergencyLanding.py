from apiInterfaces import *
from aviationDataStructures import *
from searchDataStructures import *

class SimpleProblemSolvingAgentProgram:

    def __init__(self, initial_state=None):
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, state, percept):
        raise NotImplementedError

    def formulate_goal(self, state):
        raise NotImplementedError

    def formulate_problem(self, state, goal):
        raise NotImplementedError

    def search(self, problem):
        raise NotImplementedError



class EmergencyProblem:

    def __init__(self, aircraft=None, airports=None):
        self.aircraft = aircraft
        self.airports = airports


    def run_problem(self,flight_number=None):
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

