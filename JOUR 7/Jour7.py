import os

os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 7")
data = []
with open("input.txt", "r") as variable:
  for ligne in variable:
    words = ligne.rstrip().split(" ")
    data.append(words)


def Puzzle1(Data):
  for command in Data:
    # if command[0] =="$":
    #   if command[1] =="cd":
    #     print("a")
    print(command)


Puzzle1(data)
