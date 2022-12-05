total = 0
layers = []
with open("day5.txt") as file:
    for line in file:
        if line[1] == "1":
            break
        layers.append(line[1::4])
    file.readline()
    print(layers)
    stacks = []
    for stack in zip(*layers[::-1]):
        stacks.append("".join(stack).strip())
    for line in file:
        _, count_str, _, source_str, _, destination_str = line.split(" ")
        count = int(count_str)
        source_id, destination_id = int(source_str)-1, int(destination_str)-1
        stacks[destination_id] += (stacks[source_id][-count:])
        stacks[source_id] = stacks[source_id][:-count]
    print("".join([x[-1] for x in stacks]))
            
