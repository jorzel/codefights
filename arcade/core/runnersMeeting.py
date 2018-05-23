"""
Some people run along a straight line in the same direction. They start simultaneously at pairwise distinct positions and run with constant speed (which may differ from person to person).

If two or more people are at the same point at some moment we call that a meeting. The number of people gathered at the same point is called meeting cardinality.

For the given starting positions and speeds of runners find the maximum meeting cardinality assuming that people run infinitely long. If there will be no meetings, return -1 instead.

Example

For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
runnersMeetings(startPosition, speed) = 3.

In 20 seconds after the runners start running, they end up at the same point. Check out the gif below for better understanding:
"""

			
def runnersMeetings(start_position, speed):
    _length = len(speed)
    cardinality_counter = {}
    for i in range(_length):
        for j in range(1, _length):
            position_diff = float(start_position[j] - start_position[i])
            speed_diff = float(speed[i] - speed[j])
            if speed_diff == 0:
                continue
            timestamp = str(position_diff / speed_diff)
            if not timestamp in cardinality_counter:
                cardinality_counter[timestamp] = set()
            cardinality_counter[timestamp] |= {i, j}
            if len(cardinality_counter[timestamp]) == _length:
                return _length
    results = [len(p) for p in cardinality_counter.values()]
    results.sort(reverse=True)
    if not results:
        return -1
    else:
        return results[0] if results[0] > 1 else -1
