strengths = []
screen = ["" for _ in range(6)]
with open("day10.txt") as file:
    cycle = 0
    last_check = -20
    x = 1
    for line in file:
        line = line.strip()
        x_was = x
        if line == "noop":
            cycle += 1
        else:
            cycle += 2
            x += int(line[5:])
        if cycle >= last_check + 40:
            last_check += 40
            print(cycle, x_was)
            strength = last_check * x_was
            strengths.append(strength)
print(strengths)
print(sum(strengths))
