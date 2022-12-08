import os
os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 8")

def input_per_line(file: str):
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]

data = input_per_line("input.txt")
print(data)

def num_visible_trees(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_visible_trees = 0

    for row in range(num_rows):
        for col in range(num_cols):

            tallest_row = max(map(int, grid[row]))
            row_nb_tall = row
            tallest_col = max(map(int, [grid[i][col] for i in range(num_rows)]))
            col_nb_tall = col

            print(tallest_row,tallest_col)
            print(row_nb_tall,col_nb_tall)


            if tallest_row != 0 and tallest_row != 98 and int(grid[row][col]) == tallest_row:
                visible = True
                for i in range(col):
                    if int(grid[row][i]) >= tallest_row:
                        visible = False
                        break
                if visible:
                    num_visible_trees += 1


            if tallest_col != 0 and tallest_col != 98 and int(grid[row][col]) == tallest_col:
                visible = True
                for i in range(row):
                    if int(grid[i][col]) >= tallest_col:
                        visible = False
                        break
                if visible:
                    num_visible_trees += 1

    return num_visible_trees



num_visible_trees = num_visible_trees(data)
print(num_visible_trees)
# 447 too low
# 590 too low

#min = 99*2 + 97*2