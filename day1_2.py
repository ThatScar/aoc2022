running_sum = 0
calory_counts = []
with open("day1.txt") as file:
    for line in file:
        if line.strip():
            running_sum += int(line)
        else:
            calory_counts.append(running_sum)
            running_sum = 0
print(sum(sorted(calory_counts)[-3:]))
