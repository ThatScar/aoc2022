with open("day6.txt") as file:
    line = file.readline()
    for i in range(len(line)-3):
        marker = set(line[i:i+4])
        if len(marker) >= 4:
            break
    print(i, i+4, line[i:i+4])
