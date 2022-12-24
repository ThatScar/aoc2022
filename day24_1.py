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

done = False
queue = set()
bounds = (width,height)
minute = 0
while not done:
    minute += 1
    # blizzards move; index is y,x
    blizzard_index = [[False for _ in range(width)] for _ in range(height)]
    for blizzard in blizzards:
        blizzard.pos = (blizzard.pos + blizzard.direction + bounds) % bounds
        blizzard_index[blizzard.pos[1]][blizzard.pos[0]] = True
    # positions check for blizzards and enqueue new positions
    new_queue = set()
    queue.add((0,0))
##    successful_pos = []
    for pos in queue:
        pos = numpy.array(pos)
        if (pos == (width-1,height)).all():
            done = True
            break
        elif (bounds <= pos).any() or (pos < (0,0)).any():
            continue
        elif blizzard_index[pos[1]][pos[0]]:
            continue
        else:
##            successful_pos.append(tuple(pos))
            new_queue.add(tuple(pos))
            for direction in directions:
                new_queue.add(tuple(pos + direction))
    queue = new_queue
    print(minute)
##    for i in range(height):
##        line = ""
##        for j in range(width):
##            char = "."
##            if (j,i) in successful_pos:
##                char = "E"
##            if blizzard_index[i][j]:
##                char = "v"
##            line += char
##        print(line)
