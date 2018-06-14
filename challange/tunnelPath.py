"""
Uh oh! You've slept through your alarm and it looks like you'll be late for your shift with the terraforming crew!

Fortunately, from your experience living on Mars, you've identified an underground network of tunnels formed by lava tubes. It's risky, but if you use the tunnels as a shortcut, it might just get you there on time.

All tunnels meet underground at a common point, and for each tunnel, we know the coordinates of the entry point and the distance to this junction. For example, we could represent the following map by tunnels = [[1, 2, 9], [2, 7, 5], [8, 3, 4]]:

tunnel network

In this case, the underground distance from (1, 2) to (2, 7) would be 9 + 5 = 14. The underground distance from (2, 7) to (8, 3) would be 5 + 4 = 9.

Given the startPoint (coordinates of where you live), the endPoint (coordinates of your destination), and tunnels (a list of coordinates and distances for each tunnel), find the shortest total distance you'll need to travel. All above-ground travel is measured according to Manhattan distance.

Note: you can pass through the coordinates of a tunnel entrance without entering the tunnel, and it's also possible that there's a tunnel entrance at your start or end point.

Example

For startPoint = [7, 2], endPoint = [1, 8], and tunnels = [[1, 6, 2], [7, 3, 8], [4, 1, 3]], the output should be tunnelPath(startPoint, endPoint, tunnels) = 11.

path example

Although there's a tunnel entrance right next to your starting point (at (7, 3)), it's a very long tunnel. It would be faster to take a detour and go through the tunnel at (4, 1), emerging at (1, 6), for a total distance of 4 + 3 + 2 + 2 = 11. Note that the above-ground distance would be 12, so taking the tunnel would be shorter."""


def _get_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def get_distance(point, tunnel):
    distance = _get_distance(point, tunnel[:2])
    distance += tunnel[2]
    return distance

def tunnelPath(startPoint, endPoint, tunnels):
    ground = _get_distance(startPoint, endPoint)
    _length = len(tunnels)
    min_to_hub = ground
    min_from_hub = ground
    for t in tunnels:
        to_hub = get_distance(startPoint, t)
        if to_hub < min_to_hub:
            min_to_hub = to_hub
        from_hub = get_distance(endPoint, t)
        if from_hub < min_from_hub:
            min_from_hub = from_hub
    tunnel_path = min_from_hub + min_to_hub
    return ground if ground < tunnel_path else tunnel_path
            