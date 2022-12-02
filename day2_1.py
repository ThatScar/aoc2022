score_total = 0
score_table = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
    }
with open("day2.txt") as file:
    for line in file:
        score_total += score_table[line.strip()]
        print(score_total)
print(score_total)
