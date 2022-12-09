import numpy

directions = {"R":(1,0),"U":(0,-1),"L":(-1,0),"D":(0,1)}

knot_count = 10
knots = [numpy.array((0,0)) for _ in range(knot_count)]
visited = set()
with open("day9.txt") as file:
    for line in file:
        direction, amount = line.strip().split()
        amount = int(amount)
        speed = directions[direction]
        for i in range(amount):
            knots[0] += speed
            for i in range(knot_count-1):
                tail = knots[i+1]
                target = knots[i]
                if abs(target[0] - tail[0]) >= 2 or abs(target[1] - tail[1]) >= 2:
                    offset = tuple(min(1, max(-1, to-x)) for x,to in zip(tail, target))
                    knots[i+1] += offset
            visited.add(tuple(knots[-1]))
print(len(visited))
