import ast

max_depth = 5
def depthify(i, depth):
    if depth >= max_depth:
        return i
    else:
        return [depthify(i, depth+1)]

def reshape(pack, depth):
    for i in range(len(pack)):
        if type(pack[i]) is int:
            pack[i] = depthify(pack[i], depth)
        else:
            reshape(pack[i], depth+1)

divider1 = [[depthify(2,1)]]
divider2 = [[depthify(6,1)]]
packets = [divider1, divider2]
with open("day13.txt") as file:
    for line in file:
        if not line.strip():
            continue
        packet = ast.literal_eval(line)
        reshape(packet,0)
        packets.append(packet)

packets = sorted(packets)
for packet in packets:
    print(packet)
a, b = packets.index(divider1), packets.index(divider2)
print(a, b)
print((a+1)*(b+1))
