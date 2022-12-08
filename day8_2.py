import numpy
import functools

with open("day8.txt") as file:
    tree_grid = []
    for tree_line in file:
        grid_line = []
        tree_grid.append(grid_line)
        for tree in tree_line.strip():
            grid_line.append(int(tree))

i = numpy.identity(2,dtype=int)
r = numpy.array([[0,-1],[1,0]]) #1/4 of a turn
transforms = [i, r, r.dot(r), r.dot(r).dot(r)]

best_score = 0
for y, line in enumerate(tree_grid):
    for x, tree in enumerate(line):
        scores = []
        for t in transforms:
            ray_step = 0
            while True:
                ray_step += 1
                ray = t.dot((0, ray_step))
                x2,y2 = (x,y) + ray
                if x2 < 0 or len(line) <= x2 or y2 < 0 or len(tree_grid) <= y2:
                    ray_step -= 1
                    break
                if tree_grid[y2][x2] >= tree:
                    break
            scores.append(ray_step)
        score = functools.reduce(lambda x,y: x*y, scores)
        if score > best_score:
            print(x,y,scores)
            best_score = score

print(best_score)


