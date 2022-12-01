sum = 0
best = 0
with open("day1.txt") as file:
    for line in file:
        if line.strip():
            sum += int(line)
        else:
            best = max(best, sum)
            print(sum)
            sum = 0
print(best)
