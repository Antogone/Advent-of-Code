import os
import pandas as pd

os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 4")
with open("input.txt", "r") as variable:
  data = variable.readlines()

val = 0
val2 = 0
for i in data:
    i = i.rstrip()
    z1, z2 = i.split(",")
    z1_d, z1_f = map(int, z1.split("-"))
    z2_d, z2_f = map(int, z2.split("-"))

    if ((z2_d >= z1_d) and (z2_f <= z1_f)) or ((z1_d >= z2_d) and (z1_f <= z2_f)):
        val +=1

    if ((z1_d <= z2_d <= z1_f) or (z1_d <= z2_f <= z1_f)) or ((z2_d <= z1_d <= z2_f) or (z2_d <= z1_f <= z2_f)):
        val2 += 1


print("Valeur Puzzle 1 = ",val)
print("Valeur Puzzle 2 = ",val2)

