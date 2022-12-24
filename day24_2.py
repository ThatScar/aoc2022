from dataclasses import dataclass
import numpy

@dataclass
class Blizzard:
    pos: numpy.ndarray      #x,y where -1,-1 is a wall at top-left
    direction: numpy.ndarray

left, right, up, down = directions = ((-1,0), (1,0), (0,-1), (0,1))
blizzards = []
with open("day24.txt") as file:
    line = file.readline().strip()
    width = len(line)-2
    for i, line in enumerate(file):
        line = line.strip()
        for j, char in enumerate(line[1:-1]):
            pos = numpy.array((j,i))
            if char == "#":
                height = i
                break
            elif char == ".":
                pass
            elif char == "<":
                blizzards.append(Blizzard(pos, left))
            elif char == ">":
                blizzards.append(Blizzard(pos, right))
            elif char == "^":
                blizzards.append(Blizzard(pos, up))
            elif char == "v":
                blizzards.append(Blizzard(pos, down))

state = 0
queue = set()
bounds = (width,height)
minute = 0
while state < 3:
    minute += 1
    # blizzards move; index is y,x
    blizzard_index = [[False for _ in range(width)] for _ in range(height)]
    for blizzard in blizzards:
        blizzard.pos = (blizzard.pos + blizzard.direction + bounds) % bounds
        blizzard_index[blizzard.pos[1]][blizzard.pos[0]] = True
    # positions check for blizzards and enqueue new positions
    new_queue = set()
    if state == 0 or state == 2:
        queue.add((0,0))
    if state == 1:
        queue.add((width-1,height-1))
    for pos in queue:
        pos = numpy.array(pos)
        if (state == 0 or state == 2) and (pos == (width-1,height)).all()\
                        or state == 1 and (pos == (0,-1)).all():
            state += 1
            new_queue = set()
            break
        elif (bounds <= pos).any() or (pos < (0,0)).any():
            continue
        elif blizzard_index[pos[1]][pos[0]]:
            continue
        else:
            new_queue.add(tuple(pos))
            for direction in directions:
                new_queue.add(tuple(pos + direction))
    queue = new_queue
    print(state, minute)
