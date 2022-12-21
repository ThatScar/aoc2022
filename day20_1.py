original = []
id0 = None
with open("day20.txt") as file:
    for line in file:
        number = int(line)
        if number == 0:
            id0 = len(original)
        original.append(number)
size = len(original)
print("size",size)
id_mix = [x for x in range(size)]
source = 0
for i, number in enumerate(original):
    while i != id_mix[source]:
        source += 1
    destination = (source + number + size-2)%(size-1)+1
    if source < (destination+size)%size:
        id_mix = id_mix[:source] + id_mix[source+1:destination+1] + [id_mix[source]] + id_mix[destination+1:]
    else:
        id_mix = id_mix[:destination] + [id_mix[source]] + id_mix[destination:source] + id_mix[source+1:]
    #print(f"{number} moves between {original[id_mix[destination-1]]} and {original[id_mix[(destination+1)%size]]}", source < (destination+size)%size)
    #print(", ".join([str(original[j]) for j in id_mix]))

id0_mixed = id_mix.index(id0)
a, b, c = (original[id_mix[(id0_mixed + x)%size]] for x in [1000,2000,3000])
print(a,b,c, a+b+c)
