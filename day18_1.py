wall_set = set()
with open("day18.txt") as file:
    for line in file:
        x,y,z = (int(n) for n in line.split(","))
        walls = [(x,y,z,"x"), (x+1,y,z,"x"), (x,y,z,"y"), (x,y+1,z,"y"), (x,y,z,"z"), (x,y,z+1,"z")]
        for wall in walls:
            if wall in wall_set:
                wall_set.remove(wall)
            else:
                wall_set.add(wall)
print(len(wall_set))
