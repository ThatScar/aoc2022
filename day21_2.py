import numpy

max_size = 2
def new_poly():
    return numpy.zeros(max_size, dtype=float)

yells = {}
non_zero = []
def eval_yell(name):
    yell = yells[name]
    if type(yell) is numpy.ndarray:
        result = yell
    elif " " in yell:
        pre1, op, pre2 = yell.split(" ")
        var1, var2 = eval_yell(pre1), eval_yell(pre2)
        if name == "root":
            print(var1)
            print(var2)
            result = var1 - var2
        elif op == "+":
            result = var1 + var2
        elif op == "-":
            result = var1 - var2
        elif op == "*":
            poly = new_poly()
            assert(var1[1] == 0. or var2[1] == 0.)
            for i in range(max_size):
                scale = var1[i]
                if 0. != scale:
                    assert(numpy.all(var2[max_size-i:] == 0.))
                    poly[i:] += scale*var2[:max_size-i]
            result = poly
        elif op == "/":
            assert(numpy.all(var2[1:] == 0.))
            result = var1 / var2[0]
        else:
            raise NotImplemented
    else:
        poly = new_poly()
        poly[0] = float(yell)
        result = poly
    #yells[name] = result
    if result[1] != 0.:
        print(name, result)
    return result

with open("day21.txt") as file:
    for line in file:
        name, yell = line.strip().split(": ")
        yells[name] = yell

humn = new_poly()
humn[1] = 1
yells["humn"] = humn
root = eval_yell("root")
print(f"0 = {root[0]} + {root[1]}x")
answer = -root[0]/root[1]
print(answer)
