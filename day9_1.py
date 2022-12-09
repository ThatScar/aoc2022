import numpy

tail_state_transitions = {
    (-1,-1): {"R": (-1, 0), "U": (-1, 0), "L": ( 0,-1), "D": ( 0,-1)},
    ( 0,-1): {"R": (-1,-1), "U": ( 0, 0), "L": ( 1,-1), "D": ( 0,-1)},
    ( 1,-1): {"R": ( 0,-1), "U": ( 1, 0), "L": ( 1, 0), "D": ( 0,-1)},
    (-1, 0): {"R": (-1, 0), "U": (-1, 1), "L": ( 0, 0), "D": (-1,-1)},
    ( 0, 0): {"R": (-1, 0), "U": ( 0, 1), "L": ( 1, 0), "D": ( 0,-1)},
    ( 1, 0): {"R": ( 0, 0), "U": ( 1, 1), "L": ( 1, 0), "D": ( 1,-1)},
    (-1, 1): {"R": (-1, 0), "U": ( 0, 1), "L": ( 0, 1), "D": (-1, 0)},
    ( 0, 1): {"R": (-1, 1), "U": ( 0, 1), "L": ( 1, 1), "D": ( 0, 0)},
    ( 1, 1): {"R": ( 0, 1), "U": ( 0, 1), "L": ( 1, 0), "D": ( 1, 0)}
}

directions = {"R":(1,0),"U":(0,-1),"L":(-1,0),"D":(0,1)}

head = numpy.array((0,0))
tail_offset = (0,0)
visited = set()
with open("day9.txt") as file:
    for line in file:
        direction, amount = line.strip().split()
        amount = int(amount)
        speed = directions[direction]
        for i in range(amount):
            head += speed
            tail_offset = tail_state_transitions[tail_offset][direction]
            tail_pos = head + tail_offset
            visited.add(tuple(tail_pos))
print(len(visited))
