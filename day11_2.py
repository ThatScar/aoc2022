##def o0(old): return old * 19
##def o1(old): return old + 6
##def o2(old): return old * old
##def o3(old): return old + 3
##items = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
##operations = [o0,o1,o2,o3]
##tests = [23,19,13,17]
##branches = [(2,3),(2,0),(1,3),(0,1)]
##throws = [0,0,0,0]

def o0(old): return old * 11
def o1(old): return old + 8
def o2(old): return old * 3
def o3(old): return old + 4
def o4(old): return old * old
def o5(old): return old + 2
def o6(old): return old + 3
def o7(old): return old + 5
items = [[77, 69, 76, 77, 50, 58], [75, 70, 82, 83, 96, 64, 62], [53], [85, 64, 93, 64, 99], [61, 92, 71], [79, 73, 50, 90], [50, 89], [83, 56, 64, 58, 93, 91, 56, 65]]
operations = [o0,o1,o2,o3,o4,o5,o6,o7]
tests = [5,17,2,7,3,11,13,19]
branches = [(1,5),(5,6),(0,7),(7,2),(2,3),(4,6),(4,3),(1,0)]
throws = [0 for _ in items]

lcd = 1
for test in tests:
    lcd *= test

##for monkey, holding in enumerate(items):
##    for item in holding:
##        m_id = monkey
##        states = set()
##        states_dict = {}
##        i=0
##        while True:
##            state = (m_id, item)
##            if state in states:
##                break
##            states.add(state)
##            states_dict[state] = i
##
##            op = operations[m_id]
##            item = op(item)%lcd
##            option = 0 if (item % tests[m_id]) == 0 else 1
##            throw_to = branches[m_id][option]
##
##            if throw_to < m_id:
##                i+=1
##            m_id = throw_to
##        print(i, state)
##        break
##    break

for i in range(10000):
    for m_id, op in enumerate(operations):
        for item in items[m_id]:
            item = op(item)%lcd
            option = 0 if (item % tests[m_id]) == 0 else 1
            throw_to = branches[m_id][option]
            items[throw_to].append(item)
            #print(f"{item} to monkey {throw_to}")
        throws[m_id] += len(items[m_id])
        items[m_id] = []

    if i%100 == 0:
        print(i, throws)
        for holding in items:
            print(holding)

print("--------")
throws = sorted(throws)
print(throws)
print(throws[-1]*throws[-2])
