yells = {}
def eval_yell(name):
    yell = yells[name]
    if " " in yell:
        pre1, op, pre2 = yell.split(" ")
        var1, var2 = eval_yell(pre1), eval_yell(pre2)
        if op == "+":
            result = var1 + var2
        elif op == "-":
            result = var1 - var2
        elif op == "*":
            result = var1 * var2
        elif op == "/":
            result = var1 // var2
        else:
            raise NotImplemented
    else:
        result = int(yell)
    #yells[name] = result
    return result

with open("day21.txt") as file:
    for line in file:
        name, yell = line.strip().split(": ")
        yells[name] = yell

print(eval_yell("root"))
