min_x, min_y, max_x, max_y = 500, 0, 500, 0
structures = []
with open("day14.txt") as file:
    for line in file:
        points = line.strip().split(" -> ")
        path = []
        for point in points:
            x,y = point.split(",")
            x,y = int(x), int(y)
            min_x, min_y, max_x, max_y = min(min_x,x), min(min_y,y), max(max_x,x), max(max_y,y)
            path.append((x,y))
        structures.append(path)

min_x, min_y, max_x, max_y = min_x-1, min_y-1, max_x+1, max_y+1
scan = []
for _ in range(min_y, max_y+1):
    scan.append(list("."*(max_x-min_x+1)))

for path in structures:
    x,y = path[0]
    for point in path[1:]:
        x_to,y_to = point
        if x == x_to:
            for y_i in range(y, y_to, (y_to-y)//abs(y_to-y)):
                scan[y_i-min_y][x  -min_x] = "#"
        else:
            for x_i in range(x, x_to, (x_to-x)//abs(x_to-x)):
                scan[y  -min_y][x_i-min_x] = "#"
        x,y = x_to,y_to
    scan[y-min_y][x-min_x] = "#"

scan[0-min_y][500-min_x] = "+"
for line in scan:
    print("".join(line))

# do puzzlescript and save to day14_intermediate.txt
# count Os
def count_o():
    with open("day14_intermediate.txt") as file:
        total = 0
        for line in file:
            total += len([x for x in line if x == "o"])
        print(total)
