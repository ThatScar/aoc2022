import ast

class Packet:
    def __init__(self, packet):
        self.children = []
        for sub in packet:
            if type(sub) is list:
                sub = Packet(sub)
            self.children.append(sub)
    def __iter__(self):
        return iter(self.children)
    def __lt__(self, other):
        if type(other) is Packet:
            return self.children < other.children
        else:
            return self.children < [other]
    def __gt__(self, other):
        if type(other) is Packet:
            return self.children > other.children
        else:
            return self.children > [other]
    def __repr__(self):
        return repr(self.children)

divider1 = Packet([[2]])
divider2 = Packet([[6]])
packets = [divider1, divider2]
with open("day13.txt") as file:
    for line in file:
        if not line.strip():
            continue
        packet = Packet(ast.literal_eval(line))
        packets.append(packet)

packets = sorted(packets)
for packet in packets:
    print(packet)
a, b = packets.index(divider1), packets.index(divider2)
print(a, b)
print((a+1)*(b+1))
