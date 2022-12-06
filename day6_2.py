with open("day6.txt") as file:
    line = file.readline()
    for i in range(len(line)-3):
        marker = set(line[i:i+14])
        if len(marker) >= 14:
            break
    print(i, i+14, line[i:i+14])
