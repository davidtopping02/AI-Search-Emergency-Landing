import airportsdata
from amadeus import Client, ResponseError

#dont steal my API keys
amadeus = Client(
    client_id='mOY4RkBAqfZVg6QNyYIh23NUkENb3IAF',
    client_secret='8Oy9RqdTh0O3loQa'
) 

def setCoordinates():
    print('Enter the latitude')
    lat = input()
    print('Enter the longitude')
    long = input()
    print("Enter a search radius (max is 500")
    rad = input()
    response = amadeus.reference_data.locations.airports.get(longitude=long, latitude=lat, radius=rad)
    print(response.data)

setCoordinates()

#airports = airportsdata.load('lat')  # key is ICAO code, the default
#print(airports['48'])