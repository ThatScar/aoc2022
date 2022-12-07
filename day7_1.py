with open("day7.txt") as file:
    file_system = {}
    file_system["/"] = {"..":file_system, "direct_size": 0}
    current_dir = file_system
    
    for line in file:
        line = line.strip()
        print(line)
        if line[:4] == "$ cd":
            current_dir = current_dir[line[5:]]
        elif line == "$ ls":
            pass
        elif line[:3] == "dir":
            name = line[4:]
            current_dir[name] = {"..":current_dir, "direct_size": 0}
        else:
            size_str, _ = line.split()
            current_dir["direct_size"] += int(size_str)

print("--------------------------")
score_total = 0
def tree(name, current_dir):
    global score_total
    size = current_dir["direct_size"]
    for child_name, child in current_dir.items():
        if child_name == ".." or child_name == "direct_size":
            pass
        else:
            size += tree(child_name, child)
    print(name, size)
    if size <= 100000:
        score_total += size
    return size

tree("/", file_system["/"])
print("--------------------------")
print(score_total)
