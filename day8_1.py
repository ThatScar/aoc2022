import numpy

with open("day8.txt") as file:
    tree_grid, visible_grid = [], []
    for tree_line in file:
        grid_line, visible_line = [], []
        tree_grid.append(grid_line)
        visible_grid.append(visible_line)
        for tree in tree_line.strip():
            grid_line.append(int(tree))
            visible_line.append(False)

assert(len(tree_grid) == len(tree_grid[0])) #square grid
side_length = len(tree_grid)

i = numpy.identity(2,dtype=int)
r = numpy.array([[0,-1],[1,0]]) #1/4 of a turn
transforms = [i, r, r.dot(r), r.dot(r).dot(r)]

for t in transforms:
    for ray_line in range(1, side_length+1):
        ray_height = -1
        for ray_step in range(1, side_length+1):
            x, y = t.dot((ray_line, ray_step))
            #ray base is 1,1; grid base is 0,0
            def rebase(x): return (x+side_length)%(side_length+1)
            x, y = rebase(x), rebase(y)
            tree = tree_grid[y][x]
            if tree > ray_height:
                visible_grid[y][x] = True
                ray_height = tree
print(sum(sum(numpy.array(visible_grid))))
