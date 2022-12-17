import time

class Valve:
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels
        self.distances = {}
    def __repr__(self):
        return f"{self.name} {self.rate} {self.distances}"

valves = {}
zero, not_zero = [], []
with open("day16.txt") as file:
    for line in file:
        line = "".join([x for x in line if not x.islower() and not x.isspace()])
##        print(line)
        name = line[1:3]
        rate, tunnels = line[4:].split(";")
        rate = int(rate)
        tunnels = tunnels.split(",")
        valve = Valve(name, rate, tunnels)
        valves[name] = valve
        if rate == 0:
            zero.append(valve)
        else:
            not_zero.append(valve)

for valve in not_zero + [valves["AA"]]:
    queue = [(0, valve.name)]
    while len(queue) > 0 and len(valve.distances) < len(valves):
        distance, position = queue.pop(0)
        if position not in valve.distances:
            valve.distances[position] = distance
            for tunnel in valves[position].tunnels:
                queue.append((distance+1, tunnel))
    #prune
    for other in set(zero + [valve]):
        valve.distances.pop(other.name)

start_time = time.time()

high_score = 0
def dfs(remaining, remaining2, score, visited, last, last2, stack, stack2):
    global high_score
    if remaining < remaining2:
        remaining, remaining2 = remaining2, remaining
        last, last2 = last2, last
        stack, stack2 = stack2, stack
    if remaining < 0:
        return
    score += remaining * last.rate
    if high_score < score:
        high_score = score
##        print(score)
##        print(stack)
##        print(stack2[:-1])
##        print(f"{time.time() - start_time} seconds in")
    for name, distance in list(last.distances.items()) + [("AA", 123456789)]:
        if name not in visited:
            cost = distance + 1
            valve = valves[name]
            visited.add(name)
            stack.append(name)
            dfs(remaining-cost, remaining2, score, visited, valve, last2, stack, stack2)
            stack.pop()
            visited.remove(name)

dfs(26, 26, 0, set(), valves["AA"], valves["AA"], [], [])
print(high_score)
print("--- %s seconds ---" % (time.time() - start_time))
