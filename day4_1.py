total = 0
with open("day4.txt") as file:
    for line in file:
        a, b = tuple(line.strip().split(","))
        a1, a2 = tuple(int(x) for x in a.split("-"))
        b1, b2 = tuple(int(x) for x in b.split("-"))
        if a1 <= b1 and b2 <= a2 or b1 <= a1 and a2 <= b2:
            total += 1
            print(line.strip())
print("total:",total)
