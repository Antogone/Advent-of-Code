import os

os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 7")

def input_per_line(file: str):
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]

def find_directory_sizes(these_directory, key_to_check):
  size = 0
  for item in these_directory[key_to_check]:
    if isinstance(item, int):
      size += item
    else:
      size += find_directory_sizes(these_directory, item)
  return size


data = input_per_line("input.txt")
dir: dict = {"/1": []}
curr_dir = []
depth = 0

# PUZZLE 1
for line in data:
    if curr_dir:
        previous_dir = curr_dir[-1]
    else:
        previous_dir = ""
    commande = line.split()
    if commande[0] == "$":
        if commande[1] == "cd":
            if commande[2] == "..":
                curr_dir.pop()
                depth -= 1
            else:
                depth += 1
                curr_dir.append(commande[2] + str(depth) + previous_dir)
                dir[commande[2] + str(depth) + previous_dir] = []
    elif commande[0] == "dir":
        dir[curr_dir[-1]].append(commande[1] + str(depth + 1) + previous_dir)
    else:
        dir[curr_dir[-1]].append(int(commande[0]))


dict_file_size = {}
for directory in dir:
  size = find_directory_sizes(dir, directory)
  dict_file_size[directory] = size


file_large = []
for size in dict_file_size.values():
  if size <= 100000:
    file_large.append(size)

print("Puzzle 1 :",sum(file_large))

## PUZZLE 2

total_disk_space = 70000000
space_install = 30000000
curr_free_space = total_disk_space - dict_file_size["/1"]
space_clear = space_install - curr_free_space
print("Espace Libre :",curr_free_space)


all_directory_sizes = []
for size in dict_file_size.values():
  if size >= space_clear:
    all_directory_sizes.append(size)
all_directory_sizes = sorted(all_directory_sizes)
print("Puzzle 2 :",all_directory_sizes[0])

