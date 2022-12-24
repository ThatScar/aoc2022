import re
import numpy
import time

all_allowed = (False, False, False, False)
def dfs(remaining, resources, bots, forbidden):
    global best, aa, ba, ca, cb, da, dc
    fa, fb, fc, fd = forbidden
    final_resources = resources + bots*remaining
    score = final_resources[3]
    best = max(best, score)
    if max(ba, ca, da) <= bots[0]:
        fa = True
    if cb <= bots[1]:
        fb = True
    if dc <= bots[2]:
        fc = True
    
    if remaining >= 3 and not fa and aa <= resources[0]:
        dfs(remaining-1, resources + bots - (aa,0,0,0), bots + (1,0,0,0), all_allowed)
        fa = True
    if remaining >= 4 and not fb and ba <= resources[0]:
        dfs(remaining-1, resources + bots - (ba,0,0,0), bots + (0,1,0,0), all_allowed)
        fb = True
    if remaining >= 3 and not fc and ca <= resources[0] and cb <= resources[1]:
        dfs(remaining-1, resources + bots - (ca,cb,0,0), bots + (0,0,1,0), all_allowed)
        fc = True
    if remaining >= 2 and not fd and da <= resources[0] and dc <= resources[2]:
        dfs(remaining-1, resources + bots - (da,0,dc,0), bots + (0,0,0,1), all_allowed)
        fd = True
    if remaining >= 1 and not (fa and fb and fc and fd):
        dfs(remaining-1, resources + bots, bots, (fa, fb, fc, fd))

product = 1
pattern = "Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\."
with open("day19.txt") as file:
    for line in file:
        match = re.match(pattern, line)
        i, aa, ba, ca, cb, da, dc = (int(n) for n in match.group(1,2,3,4,5,6,7))
        best = 0
        start_time = time.time()
        score = dfs(32, numpy.array((0,0,0,0)), numpy.array((1,0,0,0)), all_allowed)
        end_time = time.time() - start_time
        product *= best
        print(best, product)
        print(f"--- {end_time} seconds ---")
