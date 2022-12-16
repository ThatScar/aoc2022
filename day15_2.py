class Sensor:
    def __init__(self, x,y, distance):
        self.x = x
        self.y = y
        self.distance = distance
    def interval_at_y(self, y):
        sx_start = self.x - self.distance
        sx_end = self.x + self.distance
        forward_start,  forward_end  = sx_start +y-self.y, sx_end +y-self.y
        backward_start, backward_end = sx_start -y+self.y, sx_end -y+self.y
        return (max(forward_start,backward_start), min(forward_end,backward_end))

prefix = "Sensor at x="
beacon_separator = ": closest beacon is at x="
y_separator = ", y="
sensors = []
beacons = set()
with open("day15.txt") as file:
    for i, line in enumerate(file):
        sensor, beacon = line.strip()[len(prefix):].split(beacon_separator)
        sx, sy = (int(x) for x in sensor.split(y_separator))
        bx, by = (int(x) for x in beacon.split(y_separator))
        distance = abs(bx-sx) + abs(by-sy)
        sensors.append(Sensor(sx, sy, distance))
        beacons.add((bx,by))

def intervals_at_y(y):
    intervals = [sensor.interval_at_y(y) for sensor in sensors]
    #print(intervals)
    no_overlap = []
    for new in intervals:
        if new[0] > new[1]:
            continue
        #print(f"adding {new} to {no_overlap}")
        splice_to = len(no_overlap)
        splice_from = 0
        left = new[0]
        right = new[1]
        for i, existing in enumerate(no_overlap):
            if new[0] <= existing[1]:
                splice_to = min(splice_to, i)
                left = min(left, existing[0])
            if existing[0] <= new[1]:
                splice_from = max(splice_from, i+1)
                right = max(right, existing[1])
        no_overlap = no_overlap[:splice_to] + [(left,right)] + no_overlap[splice_from:]
    return no_overlap

##def print_row(y, window=None):
##    intervals = intervals_at_y(y)
##    left, right = zip(*intervals)
##    row = ""
##    if not window:
##        window = range(min(left)-1, max(right)+2)
##    for i in window:
##        char = "."
##        for interval in intervals:
##            if interval[0] <= i and i <= interval[1]:
##                char = "#"
##                if y == 11 and i == 14:
##                    index = intervals.index(interval)
##                    print(i, y, interval[0], interval[1], index, sensors[index].distance)
##                break
##        for sensor in sensors:
##            if sensor.y == y and sensor.x == i:
##                char = "S"
##                break
##        row += char
##    row += str(y)
##    print(row)
##    return row
##for y in range(0,21):
##    print_row(y, range(0,21))

def count_row(y):
    intervals = intervals_at_y(y)
    total = 0
    for interval in intervals:
        total += interval[1]+1-interval[0]
    beacons_at_row = [x for x in beacons if x[1] == y]
    print("beacons_at_row",beacons_at_row)
    total -= len(beacons_at_row)
    print("total",total)

def find_beacon(max_coord):
    for y in range(0,max_coord+1):
        if y%10000 == 0:
            print(f"{y*100//max_coord}%")
        intervals = intervals_at_y(y)
        x = 0
        for interval in intervals:
            if x < interval[0]:
                print(f"found at {x}, {y}, score {x*4000000 + y}")
            x = interval[1]+1
