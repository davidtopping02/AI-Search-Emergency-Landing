from aviationDataStructures import *
import requests
import json


class FlightApi:

    # Constructor which creates a new aircraft obj and sets it to the parameter
    def __init__(self, aircraft):
        self.current_aircraft = Aircraft()
        self.current_aircraft = aircraft

    # Gets required data from api, stores it in local field and returns the local field
    def get_data_from_api(self):

        print("getting flight data..."
              "")

        # parameters for the api call
        params = {
            'api_key': '3d25f7c2-f85a-4df3-8fe8-56dbc1b7ca1b',
            'flight_iata': str(self.current_aircraft.flight_number)
        }

        # attributes for api call
        method = 'ping'
        api_base = 'http://airlabs.co/api/v9/flights?'

        # api request
        api_result = requests.get(api_base + method, params)
        api_response = api_result.json()

        # error checking the api call
        if str(api_result) != '<Response [200]>':
            return None

        elif len(api_response['response']) == 0:
            return None

        # storing the api data into the aircraft object
        self.current_aircraft.departure_airport = api_response['response'][0]['dep_iata']
        self.current_aircraft.arrival_airport = api_response['response'][0]['arr_iata']
        self.current_aircraft.latitude = api_response['response'][0]['lat']
        self.current_aircraft.longitude = api_response['response'][0]['lng']
        self.current_aircraft.current_speed = api_response['response'][0]['speed']
        self.current_aircraft.altitude = api_response['response'][0]['alt']
        self.current_aircraft.dir = api_response['response'][0]['dir']
        self.current_aircraft.calc_direction()


        # prints entire contents of json call
        # print(json.dumps(api_response, indent=4, sort_keys=True))
        return self.current_aircraft
