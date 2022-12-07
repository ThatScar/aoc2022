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
dir_sizes = []
def tree(name, current_dir):
    global dir_sizes
    size = current_dir["direct_size"]
    for child_name, child in current_dir.items():
        if child_name == ".." or child_name == "direct_size":
            pass
        else:
            size += tree(child_name, child)
    print(name, size)
    dir_sizes.append(size)
    return size

total_space_used = tree("/", file_system["/"])
to_delete = total_space_used - 40000000
print("--------------------------")
print(min(x for x in dir_sizes if x >= to_delete)) #ačiū Tomui Brežinskui
