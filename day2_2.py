score_total = 0
score_table = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
    }
with open("day2.txt") as file:
    for line in file:
        score_total += score_table[line.strip()]
        print(score_total)
print(score_total)
