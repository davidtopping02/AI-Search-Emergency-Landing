import math

#two points for testing purposes
a = (52.2296756, 21.0122287)
b = (52.40637, 16.9251681)

def distanceBetweenTwoPoints(startPoint, endPoint):

    R = 6371.0 #radius of the earth

    #get lat and long from coordinate tuple
    lat1 = math.radians(startPoint[0])
    lon1 = math.radians(startPoint[1])
    lat2 = math.radians(endPoint[0])
    lon2 = math.radians(endPoint[1])

    #difference in lat and long
    dlat = lat1 - lat2
    dlon = lon1 - lon2

    #plug values into haversine equation
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance
    
def bearingBetweenTwoPoints(startPoint, endPoint):

    lat1 = math.radians(startPoint[0])
    lat2 = math.radians(endPoint[0])

    #snippet of code from https://gist.github.com/jeromer/2005586
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

    #print(compass_bearing, "degrees")
    return compass_bearing
    """
    -----CODE UNDER TESTING IGNORE------------
    if compass_bearing > 0 and compass_bearing < 90:
        n_dist = (distance*math.sin(compass_bearing))
        e_dist = (distance*math.cos(compass_bearing))

        print(n_dist, "km northward")
        print(e_dist, " km eastward")
            
    elif compass_bearing > 90 and compass_bearing < 180:
        s_dist = (distance*math.sin(compass_bearing))
        e_dist = (distance*math.cos(compass_bearing))
        print(s_dist, "km southward")
        print(e_dist, " km eastward")
    elif compass_bearing > 180 and compass_bearing < 270:
        s_dist = (distance*math.sin(((360.0 - compass_bearing)))
        w_dist = (distance*math.cos(360 - compass_bearing))
        print(s_dist, "km southward")
        print(w_dist, " km westward")
    elif compass_bearing > 270 and compass_bearing < 360:
        n_dist = (distance*math.sin(360 - compass_bearing))
        w_dist = (distance*math.cos(360 - compass_bearing))
        print(n_dist, " km northward")
        print(w_dist, " km westward")
"""
#code used for testing
print(distanceBetweenTwoPoints(a, b), " km")
print(bearingBetweenTwoPoints(a, b), "degrees")

