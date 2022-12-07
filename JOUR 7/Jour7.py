import os

os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 7")
data = []
with open("input.txt", "r") as variable:
  for ligne in variable:
    words = ligne.rstrip().split(' ')
    data.append(words)



for line in data:
    if line[0] == "$":
        if line[1] =="cd":
            curr_dir = line[-1]
            listing = 0
        if line[1] == "ls":
            listing = 1
    else:
        print(curr_dir)
        if line[0] != "dir":
            print(line)
        else:
            print(line)


# pseudo_tree = {}
# current_dir = '/'
# for line in data:
#     tokens = line.split(' ')
#     if tokens[0] == "$":
#       command = tokens[1]
#       args = tokens[2:]
#       if command ==
#       pseudo_tree.update({'command': command, 'taille': None, 'name': args, 'type' : "command"})
#     else :
#       args = tokens[0:]
#       if
#       pseudo_tree.update({'command': command, 'taille': args[0], 'name': args[1], 'type' : "fichier"})
#     print(pseudo_tree)
