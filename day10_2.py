strengths = []
screen = ["" for _ in range(6)]
def cathode(cycle, x):
    row = cycle//40
    char = "#" if abs((cycle%40)-x) <= 1 else " "
    screen[row] += char
    
with open("day10.txt") as file:
    cycle = 0
    last_check = -20
    x = 1
    for line in file:
        line = line.strip()
        x_was = x
        if line == "noop":
            cathode(cycle, x)
            cycle += 1
        else:
            cathode(cycle, x)
            cycle += 1
            cathode(cycle, x)
            cycle += 1
            x += int(line[5:])
        if cycle >= last_check + 40:
            last_check += 40
            print(cycle, x_was)
            strength = last_check * x_was
            strengths.append(strength)
print(strengths)
print(sum(strengths))
for line in screen:
    print(line)
