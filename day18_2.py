import numpy

min_x, min_y, min_z, max_x, max_y, max_z = 1000, 1000, 1000, -1000, -1000, -1000
cubes = []
with open("day18.txt") as file:
    for line in file:
        x,y,z = (int(n) for n in line.split(","))
        cubes.append((x,y,z))
        min_x, min_y, min_z, max_x, max_y, max_z = min(min_x, x-1), min(min_y, y-1), min(min_z, z-1), max(max_x, x+1), max(max_y, y+1), max(max_z, z+1)
print(min_x, min_y, min_z, max_x, max_y, max_z)

lava  = [[[False for _ in range(min_z,max_z+1)] for _ in range(min_y,max_y+1)] for _ in range(min_x,max_x+1)]
steam = [[[False for _ in range(min_z,max_z+1)] for _ in range(min_y,max_y+1)] for _ in range(min_x,max_x+1)]

for x,y,z in cubes:
    lava[x-min_x][y-min_y][z-min_z] = True
len_x, len_y, len_z = len(lava), len(lava[0]), len(lava[0][0])

neighbour_offsets = numpy.array([(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)])

total = 0
queue = [(0,0,0)]
while queue:
    x,y,z = pos = queue.pop(0)
    if len_x <= x or x < 0 or len_y <= y or y < 0 or len_z <= z or z < 0:
        continue
    elif lava[x][y][z]:
        total += 1
        continue
    elif steam[x][y][z]:
        continue
    else:
        steam[x][y][z] = True
        for offset in neighbour_offsets:
            queue.append(pos + offset)

print(total)
