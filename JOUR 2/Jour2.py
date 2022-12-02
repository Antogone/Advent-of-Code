import os
os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 2")


####PUZZLE 1
with open("input.txt", "r") as variable:
  contenu = variable.readlines()

value = 0
for i in range(len(contenu)):
    valeur = contenu[i].replace("\n","").split(" ")
    pts = 0
    match valeur[0]:
        case "A":
            adv = 1
        case "B":
            adv = 2
        case "C":
            adv = 3

    match valeur[1]:
        case "X": #ROCK
            moi = 1
        case "Y": #PAPER
            moi = 2
        case "Z": #SCISSOR
            moi = 3
    if moi == adv: # DRAW
        pts = moi + 3
    if moi == 1 and adv == 2: #Rock vs paper
        pts = moi + 0
    if moi == 1 and adv == 3: #Rock vs Scissor
        pts = moi + 6
    if moi == 2 and adv == 1: # Paper vs rock
        pts = moi + 6
    if moi == 2 and adv == 3: # papier vs Scissor
        pts = moi + 0
    if moi == 3 and adv == 2: #Scissor vs Paper
        pts = moi + 6
    if moi == 3 and adv == 1: #scissor vs rock
        pts = moi + 0
    value = value + pts
print("Value :",value)

#### PUZZLE 2
with open("input2.txt", "r") as variable:
  contenu2 = variable.readlines()

total = 0
for i in range(len(contenu2)):
    valeur = contenu2[i].replace("\n","").split(" ")
    match valeur[0]:
        case "A":
            adv = 1
        case "B":
            adv = 2
        case "C":
            adv = 3

    match valeur[1]:
        case "X": #LOSE
            moi = 1
        case "Y": #DRAW
            moi = 2
        case "Z": #WIN
            moi = 3

    if moi == 1: #LOSE
        if adv == 1:
            pts = 0 + 3
        elif adv ==2 :
            pts = 0 + 1
        elif adv ==3 :
            pts = 0+ 2

    if moi == 2: #DRAW
        if adv == 1:
            pts = 3 + adv
        elif adv == 2:
            pts = 3 + adv
        elif adv == 3:
            pts = 3 + adv
    if moi == 3: #WIN
        if adv == 1:
            pts = 6 + 2
        elif adv == 2:
            pts = 6 + 3
        elif adv == 3:
            pts = 6 + 1

    total = total + pts

print("TOTAL :",total)
