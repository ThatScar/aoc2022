score_total = 0
with open("day3.txt") as file:
    while True:
        group = (file.readline().strip(), file.readline().strip(), file.readline().strip())
        if group[0] == "":
            break
        badges = set(group[0]) & set(group[1]) & set(group[2])
        for item in badges:
            char = ord(item)
            print(item)
            priority = (char&31) + (((char&32)>>5)^1)*26
            print(priority)
            score_total+=priority
print("total:",score_total)
