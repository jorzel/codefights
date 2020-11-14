"""
When Autodesk was designing a new rail tunnel, they enlisted the help of architecture, engineering, and design consultancy Norconsult, which helped reduce the risk by applying advanced technology to a critical-yet-cumbersome design requirement - the railway signaling system. To prevent costly construction delays due to inadequate signs and signals, Norconsult used 3D modeling and VR gamification in the infrastructure design, in order to help foresee potential design problems.

Now it's time to test the system, and your task is to find the best stations for testing. You've received the stations list from your co-workers, which contains the names of at least 2 different stations, and you've been instructed to find the closest pair of stations from the list. Return the distance between these stations in the form of a floating-point numerical value.

We assume that the distance between two stations is the Euclidian distance between their coordinates (latitude and longitude).

Useful APIs

For this task, you can use the following APIs or any other public APIs that provide the necessary functionality.

Transport API.
Note that you are not allowed to access resources created specifically for solving this task (like your own service).

You can access the Transport API with the following parameters.

App ID: 8b9cd4d9, Key: 69eaf54e2f7d2f279a03077acab2721b.
App ID: ae6d5a90, Key: 5c6b8d92f7c423c588ab1ef7a03c1bce.
App ID: b6b818ca, Key: 03e4aec30ef27c673a08ea02d4567e28.
Example

For stations = ["Euston", "Mossley Hill", "Glasgow Central"], the output should be closestStations(stations) = 2.82054384773.

The closest stations are "Mossley Hill", and "Glasgow Central". The distance between them is 2.82054384773.

Input/Output

[execution time limit] 22 seconds (py3)

[input] array.string stations

The names of the stations that can be chosen. All station names contain only English letters and spaces.

Guaranteed constraints:
2 ≤ stations.length ≤ 10,
1 ≤ stations[i].length ≤ 100.

[output] float

The minimal distance between any two of the given stations. Your answer will be considered correct if the absolute error doesn't exceed 10-5.
"""



import requests
import math


def closestStations(stations):
    geolocations = calculate_geolocations(stations)
    distances = calculate_distances(stations, geolocations)
    return min(distances.values())

def calculate_distances(locations, geolocations):
    distances = {}
    for location1 in locations:
        for location2 in locations:
            location1 = location1.lower()
            location2 = location2.lower()
            pair = [location1, location2]
            pair.sort()
            tpair = tuple(pair)
            if location1 != location2 and tpair not in distances:
                geo1 = geolocations[location1]
                geo2 = geolocations[location2]
                distances[tpair] = calculate_distance(geo1[0], geo1[1], geo2[0], geo2[1])
    return distances


def calculate_geolocations(locations):
    memo = {}
    for location in locations:
        location = location.lower()
        if location not in memo:
            memo[location] = geolocation(location)
    return memo

def geolocation(location):
    app_id = '8b9cd4d9'
    key = '69eaf54e2f7d2f279a03077acab2721b'
    url = f"http://transportapi.com/v3/uk/places.json?query={location}&type=train_station&app_id={app_id}&app_key={key}"
    response_json = requests.get(url).json()['member'][0]
    return response_json['latitude'], response_json['longitude']


def calculate_distance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist