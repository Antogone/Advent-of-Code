import os
os.chdir("/Users/anto/Desktop/Advent-of-Code/JOUR 8")

with open("input.txt") as f:
    data = "\n".join([line.strip() for line in f])

def puzzl1():
    input = [[int(i) for i in x] for x in data.split("\n")]
    visible = set()
    #Comme ça on supprime les lignes que l'on ajoute qui seront deja présente

    #LIGNE
    for i in range(len(input)):
        line = input[i]
        max_tree = -1

        #Premier sens
        for j in range(len(line)):
            tree = line[j]
            if tree > max_tree:
                visible.add((i, j))
                max_tree = tree
        max_tree = -1

        #Deuxième sens
        for j in range(len(line)-1, -1, -1):
            tree = line[j]
            if tree > max_tree:
                visible.add((i, j))
                max_tree = tree

    # COLONE
    for i in range(len(input)):
        max_tree = -1

        # PREMIER SENS
        for j in range(len(input)):
            tree = input[j][i]
            #On inverse i et J

            if tree > max_tree:
                visible.add((j, i))
                max_tree = tree
        max_tree = -1

        #DEUXIEME SENS
        for j in range(len(input)-1, -1, -1):
            tree = input[j][i]
            if tree > max_tree:
                visible.add((j, i))
                max_tree = tree

    print(len(visible))


def puzzle2():
    input = [[int(i) for i in x] for x in data.split("\n")]
    best = 0

    for i in range(len(input)):

        for j in range(len(input)):

            score = 1
            base_tree = input[i][j]
            max_tree = 0

            #LIGNE PREMIER SENS
            for a in range(j+1, len(input)):
                tree = input[i][a]
                max_tree += 1
                if tree >= base_tree:
                   break

            score *= max_tree
            max_tree = 0

            #Ligne deuxieme sens
            for a in range(j-1, -1, -1):
                tree = input[i][a]
                max_tree += 1
                if tree >= base_tree:
                   break
            score *= max_tree
            max_tree = 0


            #Colonne premier sens
            for a in range(i+1, len(input)):
                tree = input[a][j]
                max_tree += 1
                if tree >= base_tree:
                   break

            score *= max_tree
            max_tree = 0

            #Colonne deuxieme sens
            for a in range(i-1, -1, -1):
                tree = input[a][j]
                max_tree += 1
                if tree >= base_tree:
                   break
            score *= max_tree

            best = max(score, best)

    print(best)

puzzl1()
puzzle2()