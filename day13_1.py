import ast

def reshape(a,b):
    for i in range(min(len(a),len(b))):
        if type(a[i]) != type(b[i]):
            if type(a[i]) is int:
                a[i] = [a[i]]
            if type(b[i]) is int:
                b[i] = [b[i]]
        if type(a[i]) is list:
            reshape(a[i],b[i])

with open("day13.txt") as file:
    i = 0
    total_count = 0
    while True:
        i += 1
        a, b, _ = file.readline(), file.readline(), file.readline()
        if not a:
            break
        a, b = ast.literal_eval(a), ast.literal_eval(b)
        reshape(a,b)
        print(a)
        print(b)
        print(a < b)
        if a < b:
            total_count += i
    print(total_count)
