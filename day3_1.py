score_total = 0
with open("day3.txt") as file:
    for line in file:
        compartment1 = set(line[:len(line)//2])
        compartment2 = set(line[len(line)//2:])
        common = compartment1 & compartment2
        for item in common:
            char = ord(item)
            print(item)
            priority = (char&31) + (((char&32)>>5)^1)*26
            print(priority)
            score_total+=priority
print("total:",score_total)
